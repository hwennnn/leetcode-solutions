---
id: balance-a-binary-search-tree
title: Balance a Binary Search Tree
description: Problem Description and Solution for Balance a Binary Search Tree
sidebar_label: 1382. Balance a Binary Search Tree
sidebar_position: 1382
---

# [1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/)

```py title=balance-a-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def storeNodes(root, arr):
            if not root: return
            
            storeNodes(root.left,arr)
            arr.append(root.val)
            storeNodes(root.right,arr)
        
        def build(arr):
            if not arr: return None
            
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = build(arr[:mid])
            root.right = build(arr[mid+1:])
            
            return root

        arr = []
        storeNodes(root,arr)
        
        return build(arr)
```


