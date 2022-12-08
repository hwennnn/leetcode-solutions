---
id: maximum-depth-of-n-ary-tree
title: Maximum Depth of N-ary Tree
description: Problem Description and Solution for Maximum Depth of N-ary Tree
sidebar_label: 559. Maximum Depth of N-ary Tree
sidebar_position: 559
---

# [559. Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree/)

```py title=maximum-depth-of-n-ary-tree.py
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root: return 0
        
        if not root.children: return 1
        
        return max(self.maxDepth(child) for child in root.children) + 1
```


