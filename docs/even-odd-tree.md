---
id: even-odd-tree
title: Even Odd Tree
description: Problem Description and Solution for Even Odd Tree
sidebar_label: 1609. Even Odd Tree
sidebar_position: 1609
---

# [1609. Even Odd Tree](https://leetcode.com/problems/even-odd-tree/)

```py title=even-odd-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root: return False
        
        q = deque()
        q.append(root)
        isEven = True
        while q:
            
            n = len(q)
            check = []
            prev = None
            while n:
                node = q.popleft()
                val = node.val
                if isEven:
                    if val % 2 == 0 or prev and val <= prev:
                        return False
                else:
                    if val % 2 or prev and val >= prev:
                        return False
                
                prev = val
                
                for t in (node.left,node.right):
                    if t:
                        q.append(t)
                
                n -= 1
                
            isEven = not isEven
                
        return True
```


