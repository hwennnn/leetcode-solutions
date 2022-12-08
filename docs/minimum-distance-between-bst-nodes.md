---
id: minimum-distance-between-bst-nodes
title: Minimum Distance Between BST Nodes
description: Problem Description and Solution for Minimum Distance Between BST Nodes
sidebar_label: 783. Minimum Distance Between BST Nodes
sidebar_position: 783
---

# [783. Minimum Distance Between BST Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)

```py title=minimum-distance-between-bst-nodes.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        A = []
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            A.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        return min(b - a for a, b in zip(A, A[1:]))
```


