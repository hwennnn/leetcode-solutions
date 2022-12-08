---
id: distribute-coins-in-binary-tree
title: Distribute Coins in Binary Tree
description: Problem Description and Solution for Distribute Coins in Binary Tree
sidebar_label: 979. Distribute Coins in Binary Tree
sidebar_position: 979
---

# [979. Distribute Coins in Binary Tree](https://leetcode.com/problems/distribute-coins-in-binary-tree/)

```py title=distribute-coins-in-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            nonlocal res
            
            if not node: return 0
            
            left, right = go(node.left), go(node.right)
            coins = left + right + node.val
            res += abs(coins - 1)
            return coins - 1
        
        go(root)
        return res
```


