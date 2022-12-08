---
id: binary-tree-maximum-path-sum
title: Binary Tree Maximum Path Sum
description: Problem Description and Solution for Binary Tree Maximum Path Sum
sidebar_label: 124. Binary Tree Maximum Path Sum
sidebar_position: 124
---

# [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

```py title=binary-tree-maximum-path-sum.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def go(node):
            nonlocal res
            if not node: return 0
            
            left = max(go(node.left), 0)
            right = max(go(node.right), 0)
            
            res = max(res, node.val + left + right)
            
            return node.val + max(left, right)
        
        go(root)
        
        return res
```


