---
id: flip-equivalent-binary-trees
title: Flip Equivalent Binary Trees
description: Problem Description and Solution for Flip Equivalent Binary Trees
sidebar_label: 951. Flip Equivalent Binary Trees
sidebar_position: 951
---

# [951. Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/)

```py title=flip-equivalent-binary-trees.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def go(node1, node2):
            if not node1 or not node2: return node1 == node2
            
            if node1.val != node2.val: return False

            return (go(node1.left, node2.left) and go(node1.right, node2.right)) or (go(node1.left, node2.right) and go(node1.right, node2.left))
        
        return go(root1, root2)
```


