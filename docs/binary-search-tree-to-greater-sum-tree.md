---
id: binary-search-tree-to-greater-sum-tree
title: Binary Search Tree to Greater Sum Tree
description: Problem Description and Solution for Binary Search Tree to Greater Sum Tree
sidebar_label: 1038. Binary Search Tree to Greater Sum Tree
sidebar_position: 1038
---

# [1038. Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)

```py title=binary-search-tree-to-greater-sum-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right: self.bstToGst(root.right)
        root.val = self.curr = self.curr + root.val
        if root.left: self.bstToGst(root.left)
        
        return root
```


