---
id: root-equals-sum-of-children
title: Root Equals Sum of Children
description: Problem Description and Solution for Root Equals Sum of Children
sidebar_label: 2236. Root Equals Sum of Children
sidebar_position: 2236
---

# [2236. Root Equals Sum of Children](https://leetcode.com/problems/root-equals-sum-of-children/)

```py title=root-equals-sum-of-children.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val
```


