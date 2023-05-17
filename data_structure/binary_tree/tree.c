#include "tree.h"

TreeNode *createTree(ElementType **data)
{
    // validation
    if (**data == '#' || **data == '\0')
    {
        (*data)++;
        return NULL;
    }
    // create root node
    TreeNode *root = (TreeNode *)malloc(sizeof(TreeNode));
    root->val = **data;
    (*data)++;
    root->left = createTree(data);
    root->right = createTree(data);
    return root;
}

void preTraversal(TreeNode *root)
{
    if (root == NULL)
        return;
    printf("%c\t", root->val);
    preTraversal(root->left);
    preTraversal(root->right);
}

void inTraversal(TreeNode *root)
{
    if (root == NULL)
        return;
    inTraversal(root->left);
    printf("%c\t", root->val);
    inTraversal(root->right);
}

void postTraversal(TreeNode *root)
{
    if (root == NULL)
        return;
    postTraversal(root->left);
    postTraversal(root->right);
    printf("%c\t", root->val);
}

void clearTree(TreeNode *root)
{
    if (root->left)
        clearTree(root->left);
    if (root->right)
        clearTree(root->right);

    free(root);
}
