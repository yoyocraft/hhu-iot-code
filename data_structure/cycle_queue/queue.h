#ifndef _QUEUE_H_
#define _QUEUE_H_

#include <limits.h>

#define COLOR(a, b) "\033[" #b "m" a "\033[0m"
#define RED(a) COLOR(a, 31)
#define GREEN(a) COLOR(a, 32)

#define ElementType int
#define Status int
#define OK 1
#define ERROR 0

typedef struct Cycle_Queue
{
    ElementType *data;
    int front, rear; // 指向队头、队尾指针
    int capacity;
} CQueue;

/// @brief 初始化循环队列
/// @param _capacity 循环队列初始化容量
/// @return Queue *
CQueue *init(int _capacity);

/// @brief val入队
/// @return OK => 入队成功， ERROR => 入队失败
Status enqueue(CQueue *cq, ElementType val);

/// @brief 队头元素出队
/// @return OK => 出队成功， ERROR => 出队失败
Status dequeue(CQueue *cq);

/// @brief 返回队头元素，如果队列为空，返回 INT_MIN
/// @return 队头元素 || INT_MIN
ElementType peekFirst(CQueue *cq);

/// @brief 返回队尾元素，如果队列为空，返回 INT_MIN
/// @return 队尾元素 || INT_MIN
ElementType peekLast(CQueue *cq);

/// @brief 返回队列中元素个数
int size(CQueue *cq);

/// @brief 判断队列是否已满
/// @return 1(true) => 队列已满
int full(CQueue *cq);

/// @brief 判断队列是否为空
/// @return 1(true) => 队列为空
int empty(CQueue *cq);

/// @brief 扩展队列容量，扩展至原有容量的两倍
/// @return OK => 扩容成功
Status expand(CQueue *cq);

/// @brief 输出队列
void output(CQueue *cq);

/// @brief 释放队列
void clear(CQueue *cq);

#endif