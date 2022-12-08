---
id: binary-tree-level-order-traversal-ii
title: Binary Tree Level Order Traversal II
description: Problem Description and Solution for Binary Tree Level Order Traversal II
sidebar_label: 107. Binary Tree Level Order Traversal II
sidebar_position: 107
---

# [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)

```py title=binary-tree-level-order-traversal-ii.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        q, res = collections.deque([(root, 0)]), []
        
        while q:
            node, lvl = q.popleft()
            
            if node:
                if len(res) < lvl + 1:
                    res.insert(0, [])
                res[-(lvl+1)].append(node.val)
                for i in (node.left,node.right):
                    if i:
                        q.append([i, lvl+1])
                
        return res
```


