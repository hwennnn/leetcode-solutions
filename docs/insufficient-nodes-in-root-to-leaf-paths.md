---
id: insufficient-nodes-in-root-to-leaf-paths
title: Insufficient Nodes in Root to Leaf Paths
description: Problem Description and Solution for Insufficient Nodes in Root to Leaf Paths
sidebar_label: 1080. Insufficient Nodes in Root to Leaf Paths
sidebar_position: 1080
---

# [1080. Insufficient Nodes in Root to Leaf Paths](https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/)

```py title=insufficient-nodes-in-root-to-leaf-paths.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if root.left == root.right:
            return None if root.val < limit else root
        
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        
        return root if root.left or root.right else None
```


