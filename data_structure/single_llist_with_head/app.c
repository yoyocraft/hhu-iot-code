/***********************************************************
* File Name: app.c
* Author: codejuzi
* Date Created: 2023-04-12
* Description: 测试类（带头节点）
************************************************************/

#include "structure.h"

int main(int argc, char const *argv[])
{
    LList *l = createLList();
    searchElement(l, 0); // l is empty
    insertLNode(l, 0);
    insertLNode(l, 1);
    insertLNode(l, 2);
    insertLNode(l, 3);
    insertLNode(l, 4);
    outputLList(l); // 4 -> 3 -> 2 -> 1 -> 0
    insertLNodeByIndex(l, 2, 5);
    outputLList(l); // 4 -> 5 -> 3 -> 2 -> 1 -> 0
    searchElement(l, 2); // count = 4
    searchElement(l, 6); // not found
    clearLList(l);
    return 0;
}
