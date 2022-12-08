---
id: binary-tree-coloring-game
title: Binary Tree Coloring Game
description: Problem Description and Solution for Binary Tree Coloring Game
sidebar_label: 1145. Binary Tree Coloring Game
sidebar_position: 1145
---

# [1145. Binary Tree Coloring Game](https://leetcode.com/problems/binary-tree-coloring-game/)

```py title=binary-tree-coloring-game.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    left, right = 0, 0
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        
        def count(node):
            if not node: return 0
            
            l, r = count(node.left), count(node.right)
            if node.val == x:
                self.left, self.right = l, r
            
            return l + r + 1
        
        count(root)
        left, right = self.left, self.right
        
        first = left > (n - left)
        second = right > (n - right)
        third = (n - left - right - 1) > (1 + left + right)
        
        return first or second or third
```


