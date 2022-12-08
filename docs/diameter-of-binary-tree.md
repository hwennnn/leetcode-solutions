---
id: diameter-of-binary-tree
title: Diameter of Binary Tree
description: Problem Description and Solution for Diameter of Binary Tree
sidebar_label: 543. Diameter of Binary Tree
sidebar_position: 543
---

# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

```py title=diameter-of-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            l, r = go(node.left), go(node.right)
            
            res = max(res, l + r)
            
            return 1 + max(l, r)
        
        go(root)
        
        return res
```


