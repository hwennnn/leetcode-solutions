---
id: binary-tree-tilt
title: Binary Tree Tilt
description: Problem Description and Solution for Binary Tree Tilt
sidebar_label: 563. Binary Tree Tilt
sidebar_position: 563
---

# [563. Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/)

```py title=binary-tree-tilt.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            left = go(node.left)
            right = go(node.right)
            
            res += abs(left - right)
            
            return node.val + left + right
        
        go(root)
        return res
```


