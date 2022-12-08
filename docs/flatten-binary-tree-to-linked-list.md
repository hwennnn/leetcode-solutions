---
id: flatten-binary-tree-to-linked-list
title: Flatten Binary Tree to Linked List
description: Problem Description and Solution for Flatten Binary Tree to Linked List
sidebar_label: 114. Flatten Binary Tree to Linked List
sidebar_position: 114
---

# [114. Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

```py title=flatten-binary-tree-to-linked-list.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.prev = None
    
    def flatten(self, root):
        if not root: return None
        
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
```


