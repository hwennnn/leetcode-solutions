---
id: range-sum-of-bst
title: Range Sum of BST
description: Problem Description and Solution for Range Sum of BST
sidebar_label: 938. Range Sum of BST
sidebar_position: 938
---

# [938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)

```py title=range-sum-of-bst.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def go(node):
            if not node: return 0
            
            return (node.val if low <= node.val <= high else 0) + go(node.left) + go(node.right)
            
        
        return go(root)
```

```cpp title=range-sum-of-bst.cpp
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
    int rangeSumBST(TreeNode* root, int low, int high) {
        return helper(root, low, high);
    }
    
    int helper(TreeNode *node, int low, int high){
        if (node == nullptr) return 0;
        int left = helper(node->left, low, high);
        int right = helper(node->right, low, high);
        
        return ((node->val >= low && node->val <= high) ? node->val : 0 ) + left + right;
    }
};
```


