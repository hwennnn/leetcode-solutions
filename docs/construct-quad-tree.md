---
id: construct-quad-tree
title: Construct Quad Tree
description: Problem Description and Solution for Construct Quad Tree
sidebar_label: 427. Construct Quad Tree
sidebar_position: 427
---

# [427. Construct Quad Tree](https://leetcode.com/problems/construct-quad-tree/)

```py title=construct-quad-tree.py
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        rows, cols = len(grid), len(grid[0])
        
        def go(x, y, n):
            if n == 1:
                return Node(grid[x][y], True, None, None, None, None)
            
            node = Node()
            topLeft = go(x, y, n // 2)
            topRight = go(x, y + n // 2, n // 2)
            bottomLeft = go(x + n // 2, y, n // 2)
            bottomRight = go(x + n // 2, y + n // 2, n // 2)

            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                node.val = topLeft.val
                node.isLeaf = True
            else:
                node.topLeft = topLeft
                node.topRight = topRight
                node.bottomLeft = bottomLeft
                node.bottomRight = bottomRight
            
            return node
        
        return go(0, 0, rows)
```


