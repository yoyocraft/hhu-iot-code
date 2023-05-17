#ifndef _TREE_H_
#define _TREE_H_

#include <stdio.h>
#include <stdlib.h>

#define ElementType char

typedef struct TreeNode
{
    ElementType val;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

/// @brief 创建二叉树
/// @param data 二叉树数据数组地址
/// @return 二叉树根节点
TreeNode *createTree(ElementType **data);

// 遍历API
void preTraversal(TreeNode *root);
void inTraversal(TreeNode *root);
void postTraversal(TreeNode *root);

/// @brief GC
void clearTree(TreeNode *root);
#endif