cmake_minimum_required(VERSION 3.25)
project(rfid-client)

set(CMAKE_CXX_STANDARD 14)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -lcurl")

# 设置curl库的路径
set(CURL_LIBRARY_DIRS ./lib/curl-8.7.1_1-win64-mingw/lib)
set(CURL_INCLUDE_DIRS ./lib/curl-8.7.1_1-win64-mingw/include)

# 添加curl库
include_directories(${CURL_INCLUDE_DIRS})
link_directories(${CURL_LIBRARY_DIRS})

add_executable(rfid-client main.cpp SerialPort.cpp stdafx.cpp)

target_link_libraries(rfid-client curl)