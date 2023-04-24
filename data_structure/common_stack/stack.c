/***********************************************************
 * File Name: stack.c
 * Author: codejuzi
 * Date Created: 2023-04-23
 * Description: 栈实现文件
 ************************************************************/
#include "stack.h"
#include <stdio.h>
#include <stdlib.h>

Stack *init(int _capacity)
{
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->data = (ElementType *)malloc(sizeof(ElementType) * _capacity);
    s->capacity = _capacity;
    s->top = -1;
    return s;
}

ElementType top(Stack *s)
{
    return empty(s) ? INT_MIN : s->data[s->top];
}

Status push(Stack *s, ElementType val)
{
    // validation
    if (!s)
        return ERROR;
    if (full(s))
    {
        // expand
        if (!expand(s))
            return ERROR;
        printf(GREEN("expand successfully! stack->capacity = (%d)\n"), s->capacity);
    }
    s->data[++(s->top)] = val;
    return OK;
}

Status pop(Stack *s)
{
    if (!s)
        return ERROR;
    if (empty(s))
    {
        printf(RED("Stack is empty!!!\n"));
        return ERROR;
    }
    s->top -= 1;
    return OK;
}

int empty(Stack *s)
{
    return s->top == -1;
}

int full(Stack *s)
{
    return s->top == s->capacity - 1;
}

Status expand(Stack *s)
{
    int exerSize = s->capacity;
    int *p;
    while (exerSize)
    {
        p = (int *)realloc(s->data, sizeof(int) * (s->capacity + exerSize));
        // 申请成功
        if (p)
            break;
        // 申请失败，折半后重新申请
        exerSize >>= 1;
    }
    if (!p)
        return ERROR;
    s->data = p;
    s->capacity += exerSize;
    return OK;
}

void output(Stack *s)
{
    if (!s)
        return;
    printf("[");
    for (int i = 0; i <= s->top; i++)
    {
        i &&printf(", ");
        printf("%d", s->data[i]);
    }
    printf("]\n");
}

void clear(Stack *s)
{
    if (!s)
        return;
    free(s->data);
    free(s);
}
