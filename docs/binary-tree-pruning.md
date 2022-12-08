---
id: binary-tree-pruning
title: Binary Tree Pruning
description: Problem Description and Solution for Binary Tree Pruning
sidebar_label: 814. Binary Tree Pruning
sidebar_position: 814
---

# [814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/)

```py title=binary-tree-pruning.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val == 0 and not node.left and not node.right: return None
            
            return node
            
        return dfs(root)
```


