/***********************************************************
 * File Name: queue.c
 * Author: codejuzi
 * Date Created: 2023-04-15
 * Description: queue.c => 实现 queue.h
 ************************************************************/
#include "queue.h"

Queue *initQueue(int _capacity)
{
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->data = (ElementType *)malloc(sizeof(ElementType) * _capacity);
    q->capacity = _capacity;
    // tail指向最后一个元素的下一个地址
    q->head = q->tail = 0;
    return q;
}

int empty(Queue *q)
{
    return q->head == q->tail;
}

int full(Queue *q)
{
    return q->tail == q->capacity;
}

Status enqueue(Queue *q, ElementType val)
{
    if (full(q))
    {
        // expand
        if (!expand(q))
            return ERROR;
        printf(GREEN("expand successfully! queue->capacity = (%d)\n"), q->capacity);
    }
    q->data[q->tail++] = val;
    return OK;
}

Status dequeue(Queue *q)
{
    if (empty(q))
    {
        printf(RED("queue is empty!!!\n"));
        return ERROR;
    }
    q->head++;
    return OK;
}

ElementType peek(Queue *q)
{
    if (empty(q))
    {
        printf(RED("queue is empty!!!\n"));
        return INT_MIN;
    }
    return q->data[q->head];
}

Status expand(Queue *q)
{
    int exerSize = q->capacity;
    int *p;
    while (exerSize)
    {
        p = (int *)reallocf(q->data, q->capacity + exerSize);
        if (p)
            break;
        // reallocf failed
        exerSize >>= 1;
    }
    if (!p)
        return ERROR;
    q->data = p;
    q->capacity += exerSize;
    return OK;
}

void output(Queue *q)
{
    if (!q)
        return;
    printf("Queue : [");
    for (int i = q->head, j = 0; i < q->tail; i++, j++)
    {
        j &&printf(", "); // 打印逗号和空格
        printf("%d", q->data[i]);
    }
    printf("]\n");
    return;
}

void clear(Queue *q)
{
    if (!q)
        return;
    free(q->data);
    free(q);
    return;
}
