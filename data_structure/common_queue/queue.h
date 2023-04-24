#ifndef _QUEUE_H_
#define _QUEUE_H_

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define ElementType int
#define Status int
#define OK 1
#define ERROR 0

#define COLOR(a, b) "\033[" #b "m" a "\033[0m"
#define GREEN(a) COLOR(a, 32)
#define RED(a) COLOR(a, 31)

typedef struct Queue
{
    ElementType *data;
    int head, tail;
    int capacity; // 队列容量
} Queue;

/// @brief 队列初始化
/// @param _capacity 初始化队列容量
/// @return 指向队列的pointer
Queue *initQueue(int _capacity);

/// @brief 返回队列是否为空
/// @return EMPTY(1) ==> 队列为空，否则不为空
int empty(Queue *q);

/// @brief 返回队列是否已满
/// @return 1 ==> 队列满
int full(Queue *q);

/// @brief push val到队列
/// @return OK => 添加成功，ERROR => 添加失败
Status enqueue(Queue *q, ElementType val);

/// @brief 弹出队列头的元素
/// @return OK => 弹出成功， ERROR => 弹出失败
Status dequeue(Queue *q);

/// @brief 返回队列头的元素，如果队列为空，返回INT_MIN
/// @return 队列头元素 || INT_MIN
ElementType peek(Queue *q);

/// @brief 扩展队列，最大扩展为原来的两倍，元素相对位置不变
/// @return OK => 扩展队列成功
Status expand(Queue *q);

/// @brief 输出队列
void output(Queue *q);

/// @brief 清空队列
void clear(Queue *q);

#endif