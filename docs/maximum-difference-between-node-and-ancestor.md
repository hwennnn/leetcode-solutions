---
id: maximum-difference-between-node-and-ancestor
title: Maximum Difference Between Node and Ancestor
description: Problem Description and Solution for Maximum Difference Between Node and Ancestor
sidebar_label: 1026. Maximum Difference Between Node and Ancestor
sidebar_position: 1026
---

# [1026. Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)

```py title=maximum-difference-between-node-and-ancestor.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, low, high):
            if not node: return high - low
            
            low = min(low, node.val)
            high = max(high, node.val)
            
            return max(dfs(node.left, low, high), dfs(node.right, low, high))
        
        return dfs(root, root.val, root.val)
```


