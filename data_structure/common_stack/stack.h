#ifndef _STACK_H_
#define _STACK_H_

#include <limits.h>

#define COLOR(a, b) "\033[" #b "m" a "\033[0m"
#define RED(a) COLOR(a, 31)
#define GREEN(a) COLOR(a, 32)

#define ElementType int
#define Status int
#define OK 1
#define ERROR 0

typedef struct Stack
{
    ElementType *data;
    // init: top = -1(栈顶指针)
    int capacity, top;
} Stack;

/// @brief 初始化栈
/// @param _capacity 栈初始大小
Stack *init(int _capacity);

/// @brief 返回栈顶元素，为空则返回返回 INT_MIN
/// @return 栈顶元素 || INT_MIN
ElementType top(Stack *s);

/// @brief 判断栈是否是空
/// @return 1(true) => 栈空
int empty(Stack *s);

/// @brief 判断栈是否已满
/// @return 1(true) => 栈满
int full(Stack *s);

/// @brief val元素压栈
/// @return OK => 压栈成功， ERROR => 压栈失败
Status push(Stack *s, ElementType val);

/// @brief 栈顶元素弹栈
/// @return OK => 弹栈成功， ERROR => 弹栈失败
Status pop(Stack *s);

/// @brief 扩展栈，最大扩展为原来的两倍，元素相对位置不变
/// @return OK => 扩展栈成功
Status expand(Stack *s);

/// @brief 输出栈信息
void output(Stack *s);

/// @brief free space
void clear(Stack *s);

#endif