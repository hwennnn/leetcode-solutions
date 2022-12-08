---
id: minimum-absolute-difference-in-bst
title: Minimum Absolute Difference in BST
description: Problem Description and Solution for Minimum Absolute Difference in BST
sidebar_label: 530. Minimum Absolute Difference in BST
sidebar_position: 530
---

# [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

```py title=minimum-absolute-difference-in-bst.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        A = []
        
        def dfs(node):
            if not node: return
            
            dfs(node.left)
            A.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        return min(b - a for a, b in zip(A, A[1:]))
```


