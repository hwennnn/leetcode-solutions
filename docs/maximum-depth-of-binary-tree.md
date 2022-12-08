---
id: maximum-depth-of-binary-tree
title: Maximum Depth of Binary Tree
description: Problem Description and Solution for Maximum Depth of Binary Tree
sidebar_label: 104. Maximum Depth of Binary Tree
sidebar_position: 104
---

# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

```py title=maximum-depth-of-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def go(node):
            if not node: return 0
            
            left, right = go(node.left), go(node.right)
            
            return 1 + max(left, right)
        
        return go(root)
```

```cpp title=maximum-depth-of-binary-tree.cpp
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
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};
```


