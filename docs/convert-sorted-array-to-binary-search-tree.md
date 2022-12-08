---
id: convert-sorted-array-to-binary-search-tree
title: Convert Sorted Array to Binary Search Tree
description: Problem Description and Solution for Convert Sorted Array to Binary Search Tree
sidebar_label: 108. Convert Sorted Array to Binary Search Tree
sidebar_position: 108
---

# [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

```py title=convert-sorted-array-to-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        
        def go(left, right):
            if left > right: return None
            
            mid = (left + right) >> 1
            
            node = TreeNode(nums[mid])
            node.left = go(left, mid - 1)
            node.right = go(mid + 1, right)
            
            return node
        
        return go(0, n - 1)
```


