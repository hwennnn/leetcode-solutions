---
id: sum-root-to-leaf-numbers
title: Sum Root to Leaf Numbers
description: Problem Description and Solution for Sum Root to Leaf Numbers
sidebar_label: 129. Sum Root to Leaf Numbers
sidebar_position: 129
---

# [129. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

```py title=sum-root-to-leaf-numbers.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def go(node, s):
            if not node: return 0
            
            if not node.left and not node.right: return s * 10 + node.val
            
            return go(node.left, s * 10 + node.val) + go(node.right, s * 10 + node.val)
        
        return go(root, 0)
```


