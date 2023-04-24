/***********************************************************
 * File Name: queue.c
 * Author: codejuzi
 * Date Created: 2023-04-24
 * Description: 循环队列实现
 ************************************************************/
#include "queue.h"
#include <stdio.h>
#include <stdlib.h>

CQueue *init(int _capacity)
{
    CQueue *cq = (CQueue *)malloc(sizeof(CQueue));
    cq->data = (ElementType *)malloc(sizeof(ElementType) * _capacity);
    // rear指向最后一个元素的下一个地址
    cq->front = cq->rear = 0;
    cq->capacity = _capacity;
    return cq;
}

Status enqueue(CQueue *cq, ElementType val)
{
    if (full(cq))
    {
        if (!expand(cq))
            return ERROR;
        printf(GREEN("expand successfully! cycle_queue->capacity = (%d)\n"), cq->capacity);
    }
    cq->data[cq->rear] = val;
    cq->rear = (cq->rear + 1) % cq->capacity;
    return OK;
}

Status dequeue(CQueue *cq)
{
    if (empty(cq))
    {
        printf(RED("cycle_queue is empty!!!\n"));
        return ERROR;
    }
    cq->front = (cq->front + 1) % cq->capacity;
    return OK;
}

ElementType peekFirst(CQueue *cq)
{
    return empty(cq) ? INT_MIN : cq->data[cq->front];
}

ElementType peekLast(CQueue *cq)
{
    return empty(cq) ? INT_MIN : cq->data[(cq->rear - 1 + cq->capacity) % cq->capacity];
}

int size(CQueue *cq)
{
    return (cq->rear - cq->front + cq->capacity) % cq->capacity;
}

int full(CQueue *cq)
{
    return (cq->rear + 1) % cq->capacity == cq->front;
}

int empty(CQueue *cq)
{
    return cq->front == cq->rear;
}

Status expand(CQueue *cq)
{
    int newCapacity = cq->capacity << 1;
    ElementType *newData = (ElementType *)malloc(sizeof(ElementType) * newCapacity);
    if (!newData)
        return ERROR;
    // 将原来的队列中的元素全部复制到新队列中
    for (int i = 0; i < cq->capacity - 1; i++)
    {
        newData[i] = cq->data[(cq->front + i) % cq->capacity];
    }

    cq->front = 0;
    cq->rear = cq->capacity - 1;
    cq->capacity = newCapacity;
    free(cq->data);
    cq->data = newData;
    return OK;
}

void output(CQueue *cq)
{
    printf("Cycle queue: [");
    for (int i = cq->front; i != cq->rear; i = (i + 1) % cq->capacity)
    {
        printf("%d", cq->data[i]);
        if ((i + 1) % cq->capacity != cq->rear)
        {
            printf(",");
        }
    }
    printf("]\n");
}

void clear(CQueue *cq)
{
    if (!cq)
        return;
    free(cq->data);
    free(cq);
}
