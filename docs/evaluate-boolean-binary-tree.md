---
id: evaluate-boolean-binary-tree
title: Evaluate Boolean Binary Tree
description: Problem Description and Solution for Evaluate Boolean Binary Tree
sidebar_label: 2331. Evaluate Boolean Binary Tree
sidebar_position: 2331
---

# [2331. Evaluate Boolean Binary Tree](https://leetcode.com/problems/evaluate-boolean-binary-tree/)

```py title=evaluate-boolean-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def go(node):
            if not node.left and not node.right:
                return node.val == 1
            
            left, right = go(node.left), go(node.right)
            
            return left or right if node.val == 2 else left and right
        
        return go(root)
```


