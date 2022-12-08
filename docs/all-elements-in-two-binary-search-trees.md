---
id: all-elements-in-two-binary-search-trees
title: All Elements in Two Binary Search Trees
description: Problem Description and Solution for All Elements in Two Binary Search Trees
sidebar_label: 1305. All Elements in Two Binary Search Trees
sidebar_position: 1305
---

# [1305. All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

```py title=all-elements-in-two-binary-search-trees.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        self.helperR(root1, res)
        self.helperR(root2, res)
        
        return sorted(res)
    
    def helperR(self, root, res):
        if not root: return
        
        res.append(root.val)
        self.helperR(root.left, res)
        self.helperR(root.right, res)
        
```


