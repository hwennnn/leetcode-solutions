---
id: convert-bst-to-greater-tree
title: Convert BST to Greater Tree
description: Problem Description and Solution for Convert BST to Greater Tree
sidebar_label: 538. Convert BST to Greater Tree
sidebar_position: 538
---

# [538. Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)

```py title=convert-bst-to-greater-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curr = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        if root.right: self.convertBST(root.right)
        root.val = self.curr = self.curr + root.val
        if root.left: self.convertBST(root.left)
        
        return root
```


