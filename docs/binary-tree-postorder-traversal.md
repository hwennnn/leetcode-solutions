---
id: binary-tree-postorder-traversal
title: Binary Tree Postorder Traversal
description: Problem Description and Solution for Binary Tree Postorder Traversal
sidebar_label: 145. Binary Tree Postorder Traversal
sidebar_position: 145
---

# [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

```py title=binary-tree-postorder-traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        
        dfs(root)
        return res
```

```cpp title=binary-tree-postorder-traversal.cpp
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
    void dfs(TreeNode* root, vector<int> &res){
        if (root == nullptr) return;
        
        dfs(root->left, res);
        dfs(root->right, res);
        res.push_back(root->val);
    }
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> res;
        dfs(root, res);
        
        return res;
    }
};
```


