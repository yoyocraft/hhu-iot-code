/***********************************************************
 * File Name: app.c
 * Author: codejuzi
 * Date Created: 2023-04-15
 * Description: 测试文件
 ************************************************************/
#include "queue.h"
#include <stdio.h>

const int QUEUE_CAPACITY = 3;

int main(int argc, char const *argv[])
{

    Queue *q = initQueue(QUEUE_CAPACITY);
    printf("peek = %d\n", peek(q)); // INT_MIN
    enqueue(q, 0);
    enqueue(q, 1);
    enqueue(q, 2);
    output(q);                      // [0, 1, 2]
    printf("peek = %d\n", peek(q)); // peek = 0
    enqueue(q, 3);                  // expand
    dequeue(q);
    dequeue(q);
    output(q);                      // [2]
    printf("peek = %d\n", peek(q)); // peek = 2
    dequeue(q);
    dequeue(q);
    output(q);  // []
    dequeue(q); // q is empty
    clear(q);
    return 0;
}
