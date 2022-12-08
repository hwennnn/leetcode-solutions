---
id: leaf-similar-trees
title: Leaf-Similar Trees
description: Problem Description and Solution for Leaf-Similar Trees
sidebar_label: 872. Leaf-Similar Trees
sidebar_position: 872
---

# [872. Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)

```py title=leaf-similar-trees.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.findleaf(root1) == self.findleaf(root2)
        
    def findleaf(self, root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return self.findleaf(root.left) + self.findleaf(root.right)
```


