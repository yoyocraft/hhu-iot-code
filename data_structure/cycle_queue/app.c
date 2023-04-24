/***********************************************************
 * File Name: app.c
 * Author: codejuzi
 * Date Created: 2023-04-24
 * Description: 循环队列测试
 ************************************************************/
#include <stdio.h>
#include "queue.h"

const int INIT_QUEUE_SIZE = 3;
int main(int argc, char const *argv[])
{
    CQueue *cq = init(INIT_QUEUE_SIZE);
    dequeue(cq); // queue is empty
    enqueue(cq, 0);
    enqueue(cq, 1);
    enqueue(cq, 2);
    output(cq);
    enqueue(cq, 3);                                // expand
    output(cq);                                    // [0, 1, 2, 3]
    printf("peekFirst(cq) = %d\n", peekFirst(cq)); // 0
    printf("peekLast(cq) = %d\n", peekLast(cq));   // 3
    dequeue(cq);
    printf("peekFirst(cq) = %d\n", peekFirst(cq)); // 1
    enqueue(cq, 4);
    enqueue(cq, 5);
    enqueue(cq, 6);
    printf("peekFirst(cq) = %d\n", peekFirst(cq)); // 1
    printf("peekLast(cq) = %d\n", peekLast(cq));   // 6
    output(cq);                                    // [1, 2, 3, 4, 5, 6]
    clear(cq);
    return 0;
}
