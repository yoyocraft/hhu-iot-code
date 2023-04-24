/***********************************************************
 * File Name: app.c
 * Author: codejuzi
 * Date Created: 2023-04-23
 * Description: 测试文件
 ************************************************************/
#include "stack.h"
#include <stdio.h>

const int INIT_SIZE = 3;

int main(int argc, char const *argv[])
{
    Stack *s = init(INIT_SIZE);
    pop(s); // stack is empty
    push(s, 0);
    push(s, 1);
    push(s, 2);
    push(s, 3); // expand the stack ==> s->size = 6
    output(s);  // [0, 1, 2, 3]
    printf("top = %d\n", top(s)); // top = 3
    pop(s);                       // 3
    output(s);                    // [0, 1, 2]
    clear(s);
    return 0;
}
