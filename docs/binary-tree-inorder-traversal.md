---
id: binary-tree-inorder-traversal
title: Binary Tree Inorder Traversal
description: Problem Description and Solution for Binary Tree Inorder Traversal
sidebar_label: 94. Binary Tree Inorder Traversal
sidebar_position: 94
---

# [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

```py title=binary-tree-inorder-traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        
        def go(node):
            if not node: return
            
            go(node.left)
            res.append(node.val)
            go(node.right)
        
        go(root)
        return res
```

```cpp title=binary-tree-inorder-traversal.cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> res;
    void helperR(TreeNode *root){
        if (root == nullptr) return;
        
        helperR(root->left);
        res.push_back(root->val);
        helperR(root->right);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        helperR(root);
        return res;
    }
    
};
```


