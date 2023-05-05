#include <stdio.h>
#include <stdlib.h>

#pragma region Color

#define COLOR(a, b) "\033[" #b "m" a "\033[0m"
#define GREEN(a) COLOR(a, 32)

#pragma endregion

#pragma region Constant

#define OK 0
#define ERROR 1
#define Status int

#pragma endregion

#pragma region LNode

/// @brief 节点
typedef struct LNode
{
    int data;
    struct LNode *next;
} LNode;

#pragma endregion

#pragma region LList

/// @brief 链表
typedef struct LList
{
    LNode *head;
    int length;
} LList;

#pragma endregion

/// @brief 创建节点
/// @return 指向新节点的指针
LNode *createLNode(int data);

/// @brief 初始化链表
/// @return 指向链表头的指针
LList *createLList();

/// @brief 插入节点（头插法）
/// @return OK => 插入成功， ERROR => 插入失败
Status insertLNode(LList *l, int data);

/// @brief 在链表的index位置插入节点
/// @return OK => 插入成功， ERROR => 插入失败
Status insertLNodeByIndex(LList *l, int index, int data);

/// @brief 输出链表
/// @param l 链表
void outputLList(LList *l);

/// @brief 释放链表
/// @param l 链表
void clearLList(LList *l);

/// @brief 根据val查询，并输出
/// @return OK => 查找到， ERROR => 链表为空 || 查询无果
Status searchElement(LList *l, int val);
