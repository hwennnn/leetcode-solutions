---
id: delete-leaves-with-a-given-value
title: Delete Leaves With a Given Value
description: Problem Description and Solution for Delete Leaves With a Given Value
sidebar_label: 1325. Delete Leaves With a Given Value
sidebar_position: 1325
---

# [1325. Delete Leaves With a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/)

```py title=delete-leaves-with-a-given-value.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, target):
        if not root: return None
        
        root.left = self.dfs(root.left, target)
        root.right = self.dfs(root.right, target)
        
        if root.left == root.right == None and root.val == target: return None
        
        return root
        
            
        
        
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        return self.dfs(root, target)
```


