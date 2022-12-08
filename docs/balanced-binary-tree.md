---
id: balanced-binary-tree
title: Balanced Binary Tree
description: Problem Description and Solution for Balanced Binary Tree
sidebar_label: 110. Balanced Binary Tree
sidebar_position: 110
---

# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

```py title=balanced-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            l, r = go(node.left), go(node.right)
            
            if abs(l - r) > 1:
                res = False
            
            return 1 + max(l, r)
        
        go(root)
        
        return res
```

```cpp title=balanced-binary-tree.cpp
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
    int dfs(TreeNode* root){
        if (root == nullptr) return 0;
        
        int left = dfs(root->left);
        int right = dfs(root->right);
        
        if (left == -1 || right == -1 || abs(left-right) > 1) return -1;
        
        return 1 + max(left, right);
    }
    
    bool isBalanced(TreeNode* root) {
        return dfs(root) != -1;
    }
};
```


