#include "stdafx.h"
#include "SerialPort.h"
#include "json.hpp"
#include <process.h>
#include <curl/curl.h>
#include <iostream>
#include <string>
#include <cmath>

using json = nlohmann::json;

UCHAR CMD[23] = {0x01, 0x17, 0xA4, 0x20, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
UCHAR CMD_WRITE[23] = {0x01, 0x17, 0xA4, 0x20, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                       0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};

std::string SERVER_URL = "http://2b79b9e9.r15.cpolar.top";
std::string SERVICE_PATH = "/user/clockin";

// region function definition

// region out line functions
void menu();

void errorTips();
// endregion

// region check functions
bool isWriteResp(UCHAR *revData, UINT readBytes);

bool isReadResp(UCHAR *revData, UINT readBytes);

bool checkIoSuccess(const UCHAR *revData);

void checkSumOut(UCHAR *buf, UCHAR len);

bool checkSumIn(const UCHAR *buf, UCHAR len);
// endregion

// region util functions
void hex2Str(const UCHAR *sSrc, UCHAR *sDest, int len);

void hexStrToByte(const UCHAR *source, UCHAR *dest, int len);
// endregion

// region interacting with the server and processing functions
int getUserIdFromBlockData(const UCHAR blockData[]);

int clockIn(int userId);

size_t writeCallback(void *contents, size_t size, size_t nums, std::string *response);

void writeMonthTime2Card(int monthClockInTime, SerialPort mySerialPort);

void handleMonthClockInTime(int monthClockInTime);
// endregion

// endregion

int main(int argc, _TCHAR *argv[])
{
    UCHAR inByte, revData[32], inData[100];
    UINT len, readBytes, i;
    INT block;

    SerialPort mySerialPort;
    system("chcp 65001");

    if (!mySerialPort.InitPort(7))
    {
        std::cout << "初始化COM7失败，请检查读写器端口是否为COM7，或者是否被其它软件打开占用！" << std::endl;
        std::cout << "按任意键后，回车退出程序！" << std::endl;
        std::cin >> inByte;
    }
    else
    {
        std::cout << "初始化成功!" << std::endl;

        while (true)
        {
            menu();
            std::cin >> inByte;
            block = -1;
            switch (inByte)
            {
            case '1':
                std::cout << "请将IC卡放读写器感应区内，输入要写入数据的块号：";
                std::cin >> block;
                if (block > 0)
                {
                    for (i = 0; i < 32; i++)
                    {
                        inData[i] = '0';
                    }
                    std::cout << "输入要写入的数据（比如 0116)：";
                    std::cin >> inData;
                    CMD[1] = 0x17;
                    CMD[2] = 0xA4;
                    CMD[4] = (UCHAR)block;
                    hexStrToByte(&inData[0], &CMD[6], 32); // 将输入的字符转成16进制字节数并拷贝到数组（命令）中
                }
                break;
            case '2':
                std::cout << std::endl
                          << "程序会等待5秒，请在5秒内放上卡！" << std::endl;
                Sleep(5000);
                std::cout << "等待结束，开始读卡！" << std::endl;
                std::cout << "请将IC卡放读写器感应区内，输入要读的块号：";
                std::cin >> block;
                if (block > 0)
                {
                    CMD[1] = 0x08;
                    CMD[2] = 0xA3;
                    CMD[4] = (UCHAR)block;
                }
                break;
            default:
                std::cout << "******输入错误！输入错误！输入错误！******" << std::endl
                          << std::endl;
                menu();
            }
            if (block > 0)
            {
                checkSumOut(CMD, CMD[1]);
                Sleep(1000);
                if (!mySerialPort.WriteData(CMD, CMD[1]))
                {
                    mySerialPort.InitPort(7);
                    mySerialPort.WriteData(CMD, CMD[1]);
                }
                Sleep(200);                         // 延时200毫秒等待读写器返回数据，延时太小可能无法接收完整的数据包
                len = mySerialPort.GetBytesInCOM(); // 获取串口缓冲区中字节数
                if (len >= 8)
                {
                    readBytes = 0;
                    do // 获取串口缓冲区数据
                    {
                        inByte = 0;
                        if (mySerialPort.ReadChar(inByte))
                        {
                            revData[readBytes] = inByte;
                            readBytes++;
                        }
                    } while (--len);

                    if (isWriteResp(revData, readBytes)) // 判断是否为写数据返回的数据包
                    {
                        bool status = checkSumIn(revData, revData[1]); // 计算校验和
                        if (status)
                        {
                            if (checkIoSuccess(revData))
                            {
                                std::cout << "写数据到数据块" << block << "成功！" << std::endl
                                          << std::endl;
                            }
                            else
                            {
                                errorTips();
                            }
                        }
                    }
                    if (isReadResp(revData, readBytes)) // 判断是否为读数据块返回的数据包
                    {
                        bool status = checkSumIn(revData, revData[1]); // 计算校验和
                        if (status)
                        {
                            if (checkIoSuccess(revData))
                            {
                                UCHAR blockData[16];
                                UCHAR temp[33];
                                std::cout << "block data: ";
                                for (i = 0; i < 16; i++)
                                {
                                    blockData[i] = revData[5 + i]; // 复制数据到数组
                                    std::cout << blockData[i];
                                }
                                std::cout << std::endl;
                                hex2Str(&blockData[0], &temp[0], 16); // 数据块数据转换为字符

                                std::cout << "读数据块成功，14扇区的数据块" << block << "数据为：" << temp << std::endl
                                          << std::endl;

                                // 读取 userId 并签到
                                int userId = getUserIdFromBlockData(temp);
                                int monthClockInTime = clockIn(userId);

                                // 下班时写数据到卡中
                                if (monthClockInTime)
                                {
                                    writeMonthTime2Card(monthClockInTime, mySerialPort);
                                    handleMonthClockInTime(monthClockInTime);
                                }
                                Sleep(5000);
                            }
                            else // 读数据块失败
                            {
                                std::cout << "读,写数据块失败,失败原因如下：" << std::endl;
                                errorTips();
                                std::cout << "未探测到卡片，请重试！" << std::endl;
                                std::cout << "程序会暂停10s，等待再次读卡！" << std::endl
                                          << std::endl;
                                Sleep(10000);
                            }
                        }
                    }
                }
                else
                {
                    std::cout << "读写器超时……，请检查读卡器的连接是否正常！" << std::endl;
                    while (len-- > 0) // 如果缓冲区中有数据，将缓冲区中数据清空
                    {
                        mySerialPort.ReadChar(inByte);
                    }
                }
            }
            else
            {
                if (std::cin.fail())
                {
                    std::cin.clear();
                    std::cin.sync();
                    std::cout << "******输入错误，请输入数字******" << std::endl
                              << std::endl;
                    menu();
                }
            }
        }
    }
}

void checkSumOut(UCHAR *buf, UCHAR len)
{
    UCHAR i, checksum = 0;
    for (i = 0; i < (len - 1); i++)
    {
        checksum ^= buf[i];
    }
    buf[len - 1] = (UCHAR)~checksum;
}

bool checkSumIn(const UCHAR *buf, UCHAR len)
{
    UCHAR i, checksum = 0;
    for (i = 0; i < (len - 1); i++)
    {
        checksum ^= buf[i];
    }
    return buf[len - 1] == (UCHAR)~checksum;
}

void hex2Str(const UCHAR *sSrc, UCHAR *sDest, int len)
{
    int i;
    char szTmp[3];

    for (i = 0; i < len; i++)
    {
        sprintf_s(szTmp, "%02X", (unsigned char)sSrc[i]);
        memcpy(&sDest[i * 2], szTmp, 2);
    }
    sDest[len * 2] = '\0';
}

void hexStrToByte(const UCHAR *source, UCHAR *dest, int len)
{
    int i;
    unsigned char highByte, lowByte;

    for (i = 0; i < len; i += 2)
    {
        highByte = toupper(source[i]);
        lowByte = toupper(source[i + 1]);

        if (highByte > 0x39)
            highByte -= 0x37;
        else
            highByte -= 0x30;

        if (lowByte > 0x39)
            lowByte -= 0x37;
        else
            lowByte -= 0x30;

        dest[i / 2] = (highByte << 4) | lowByte;
    }
}

int getUserIdFromBlockData(const UCHAR blockData[])
{
    int result = 0;
    for (int i = 0; i < 4; ++i)
    {
        result = result * 10 + (blockData[i] - '0');
    }
    return result;
}

int clockIn(int userId)
{
    std::cout << "send request userid:" << userId << std::endl;

    CURL *curl = curl_easy_init();
    if (!curl)
    {
        std::cerr << "Failed to initialize Curl" << std::endl;
        return 1;
    }
    // 创建请求参数
    std::string url = SERVER_URL + SERVICE_PATH;
    json data;
    data["userId"] = userId;
    // 将JSON数据转换为字符串
    std::string jsonStr = data.dump();
    struct curl_slist *headers = nullptr;
    headers = curl_slist_append(headers, "Content-Type: application/json");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    // 设置Curl选项
    curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, jsonStr.c_str());
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeCallback);
    // 创建响应存储变量
    std::string response;
    // 传递 response 变量作为回调函数的参数
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);
    // 发送请求并等待响应
    std::cout << "CURL send Data" << std::endl;
    int monthClockInTime = 0;
    CURLcode resp = curl_easy_perform(curl);
    if (resp != CURLE_OK)
    {
        std::cerr << "Curl request failed: " << curl_easy_strerror(resp) << std::endl;
    }
    else
    {
        // 解析正常的响应
        long statusCode;
        curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &statusCode);
        std::cout << "response: " << response << std::endl;
        json jsonResponse = json::parse(response);
        if (!jsonResponse["tag"].get<int>())
        {
            std::cout << std::endl
                      << "===> 非法用户，无权进入！" << std::endl;
        }
        if (jsonResponse["tag"].get<int>() == 1)
        {
            std::cout << std::endl
                      << "===> 上班打卡成功！" << std::endl;
        }
        if (jsonResponse["tag"].get<int>() == 2)
        {
            std::cout << std::endl
                      << "===> 下班打卡成功！" << std::endl;
        }
        if (jsonResponse.contains("monthClockInTime"))
        {
            monthClockInTime = jsonResponse["monthClockInTime"].get<int>();
        }
        if (jsonResponse.contains("attendTime"))
        {
            int attendTime = jsonResponse["attendTime"].get<int>();
            int hour = attendTime / 3600;
            int minute = (attendTime % 3600) / 60;
            int second = (attendTime % 60);
            std::cout << std::endl
                      << "本次出勤时间为："
                      << hour << "小时，"
                      << minute << "分钟，"
                      << second << "秒。"
                      << std::endl;
        }
    }
    // 清理Curl句柄
    curl_easy_cleanup(curl);
    return monthClockInTime;
}

size_t writeCallback(void *contents, size_t size, size_t nums, std::string *response)
{
    size_t totalSize = size * nums;
    response->append((char *)contents, totalSize);
    return totalSize;
}

void writeMonthTime2Card(int monthClockInTime, SerialPort mySerialPort)
{
    UINT i, len;
    INT block;
    UCHAR inByte, revData[32], inData[100];

    for (i = 0; i < 32; i++)
    {
        inData[i] = '0';
    }
    std::string str = std::to_string(monthClockInTime);
    for (int j = 0; j < str.length(); j++)
    {
        inData[j] = str[j];
    }
    block = 60;
    CMD_WRITE[1] = 0x17;
    CMD_WRITE[2] = 0xA4;
    CMD_WRITE[4] = (UCHAR)block;
    hexStrToByte(&inData[0], &CMD_WRITE[6], 32);

    checkSumOut(CMD_WRITE, CMD_WRITE[1]);

    mySerialPort.WriteData(CMD_WRITE, CMD_WRITE[1]); // 通过串口发送读数据块指令给读写器
    Sleep(1000);                                     // 延时200毫秒等待读写器返回数据，延时太小可能无法接收完整的数据包
    len = mySerialPort.GetBytesInCOM();              // 获取串口缓冲区中字节数

    UINT readBytes = 0;
    do // 获取串口缓冲区数据
    {
        inByte = 0;
        if (mySerialPort.ReadChar(inByte))
        {
            revData[readBytes] = inByte;
            readBytes++;
        }
    } while (--len);

    if (isWriteResp(revData, readBytes)) // 判断是否为写数据返回的数据包
    {
        bool status = checkSumIn(revData, revData[1]); // 计算校验和
        if (status)
        {
            if (revData[4] == 0x00) // 写数据块成功
            {
                std::cout << std::endl
                          << "写数据到15扇区的数据块" << block << "成功！" << std::endl
                          << std::endl;
            }
            else // 写数据块失败
            {
                std::cout << "读,写数据块失败,失败原因如下：" << std::endl;
                std::cout << "1. 检查IC卡是否放置在读写器的感应区内." << std::endl;
                std::cout << "2. IC卡对应扇区密码与读写器读写密码不一致." << std::endl;
                std::cout << "3. 输入的数据块值超过IC卡的最大数据块数值，比如S50卡有63个数据块." << std::endl;
                std::cout << "4. 密码控制块不可以读或写." << std::endl;
            }
        }
    }
}

bool isWriteResp(UCHAR *revData, UINT readBytes)
{
    return (revData[0] = 0x01) && (revData[1] == 8) && (revData[1] == readBytes) && (revData[2] == 0x0A4) && (revData[3] = 0x20);
}

void handleMonthClockInTime(int monthClockInTime)
{
    int power = 0, x = monthClockInTime;
    while (x > 9)
    {
        power++;
        x = x / 10;
    }
    int actualTime = monthClockInTime % int((pow(10, power)));
    int hour = actualTime / 3600;
    int minute = (actualTime % 3600) / 60;
    int second = (actualTime % 60);
    std::cout << "本自然月内出勤时间为："
              << hour << "小时，"
              << minute << "分钟，"
              << second << "秒。"
              << std::endl;
}

bool checkIoSuccess(const UCHAR *revData) { return revData[4] == 0x00; }

void errorTips()
{
    std::cout << "读,写数据块失败,失败原因可能是：" << std::endl;
    std::cout << "1. 检查IC卡是否放置在读写器的感应区内." << std::endl;
    std::cout << "2. IC卡对应扇区密码与读写器读写密码不一致." << std::endl;
    std::cout << "3. 输入的数据块值超过IC卡的最大数据块数值." << std::endl;
    std::cout << "4. 密码控制块不可以读或写." << std::endl;
}

bool isReadResp(UCHAR *revData, UINT readBytes)
{
    return (revData[0] = 0x01) && ((revData[1] == 8) || (revData[1] == 22)) && (revData[1] == readBytes) &&
           (revData[2] == 0xA3) && (revData[3] = 0x20);
}

void menu()
{
    std::cout << "=======================" << std::endl;
    std::cout << "输入 “1” 按回车键写数据块" << std::endl;
    std::cout << "输入 “2” 按回车键读数据块" << std::endl;
    std::cout << "=======================" << std::endl;
}
