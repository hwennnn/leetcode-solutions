---
id: binary-tree-preorder-traversal
title: Binary Tree Preorder Traversal
description: Problem Description and Solution for Binary Tree Preorder Traversal
sidebar_label: 144. Binary Tree Preorder Traversal
sidebar_position: 144
---

# [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

```py title=binary-tree-preorder-traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node: return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res
```

```cpp title=binary-tree-preorder-traversal.cpp
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
    
    void helperR(TreeNode* root){
        if (root == nullptr) return;
        
        res.push_back(root->val);
        helperR(root->left);
        helperR(root->right);
    }
    
    vector<int> preorderTraversal(TreeNode* root) {
        helperR(root);
        
        return res;
    }
};
```


