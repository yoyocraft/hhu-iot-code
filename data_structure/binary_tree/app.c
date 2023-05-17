#include "tree.h"
#include <stdio.h>

int main(int argc, char const *argv[])
{
    ElementType *data = "ABC##DE#G##F##H##";
    TreeNode *root = createTree(&data);

    printf("===> preorder traversal: \n");
    preTraversal(root);
    printf("\n<=== \n");

    printf("===> inorder traversal: \n");
    inTraversal(root);
    printf("\n<=== \n");

    printf("===> postorder traversal: \n");
    postTraversal(root);
    printf("\n<=== \n");

    clearTree(root);
    return 0;
}
