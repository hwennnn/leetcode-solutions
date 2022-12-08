---
id: lowest-common-ancestor-of-a-binary-tree
title: Lowest Common Ancestor of a Binary Tree
description: Problem Description and Solution for Lowest Common Ancestor of a Binary Tree
sidebar_label: 236. Lowest Common Ancestor of a Binary Tree
sidebar_position: 236
---

# [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

```py title=lowest-common-ancestor-of-a-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if root in (None, p, q): return root
            
            left, right = dfs(root.left), dfs(root.right)
            
            return root if left and right else left or right
            
        return dfs(root)
```


