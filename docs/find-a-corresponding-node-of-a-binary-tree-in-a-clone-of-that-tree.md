---
id: find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree
title: Find a Corresponding Node of a Binary Tree in a Clone of That Tree
description: Problem Description and Solution for Find a Corresponding Node of a Binary Tree in a Clone of That Tree
sidebar_label: 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
sidebar_position: 1379
---

# [1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/)

```py title=find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def go(a, b):
            if not a: return None
            
            if a is target: return b
            
            return go(a.left, b.left) or go(a.right, b.right)
        
        return go(original, cloned)
```


