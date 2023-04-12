/***********************************************************
* File Name: structure.c
* Author: codejuzi
* Date Created: 2023-04-12
* Description: 方法实现文件 => "structure.c"
************************************************************/
#include "structure.h"

/// @brief
/// @param data
/// @return
LNode *createLNode(int data)
{
    LNode *node = (LNode *)malloc(sizeof(LNode));
    node->data = data;
    node->next = NULL;
    return node;
}

LList *createLList()
{
    LList *l = (LList *)malloc(sizeof(LList));
    l->length = 0;
    return l;
}

Status insertLNode(LList *l, int data)
{
    LNode *node = createLNode(data);
    l->length++;
    node->next = l->head;
    l->head = node;
    return OK;
}

Status insertLNodeByIndex(LList *l, int index, int data)
{
    // validation
    if (index <= 0 || index > l->length)
    {
        printf(GREEN("index不合法!\n"));
        return ERROR;
    }
    LNode *p = l->head;
    // 1 ~ index - 1：不带头节点， index=2,只需要移动一位，以此类推
    for (int i = 1; i < index - 1; i++)
    {
        p = p->next;
    }
    LNode *newNode = createLNode(data);
    newNode->next = p->next;
    p->next = newNode;
    return OK;
}

void outputLList(LList *l)
{
    // validation
    if (!l)
        return;
    printf("LinkedList(%d) = [", l->length);
    for (LNode *p = l->head; p; p = p->next)
    {
        printf("%d->", p->data);
    }
    printf("NULL]\n");
}

void clearLList(LList *l)
{
    LNode *p = l->head;
    if (!p)
    {
        free(l);
        return;
    }
    for (; p;)
    {
        LNode *tmp = p->next;
        free(p);
        p = tmp;
    }
    free(l);
}

Status searchElement(LList *l, int val)
{
    if (!l->head)
    {
        printf(GREEN("链表为空！\n"));
        return ERROR;
    }
    int count = 1;
    LNode *p = l->head;
    while (p && p->data != val)
    {
        p = p->next;
        ++count;
    }
    if (!p)
    {
        printf(GREEN("查询无果！\n"));
        return ERROR;
    }
    printf("找到值p->data = %d,在链表中是第%d位\n", val, count);
    return OK;
}