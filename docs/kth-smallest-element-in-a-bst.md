---
id: kth-smallest-element-in-a-bst
title: Kth Smallest Element in a BST
description: Problem Description and Solution for Kth Smallest Element in a BST
sidebar_label: 230. Kth Smallest Element in a BST
sidebar_position: 230
---

# [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

```py title=kth-smallest-element-in-a-bst.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = -1
        self.k = k
        
        def dfs(node):
            if node.left: dfs(node.left)
                
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            
            if node.right: dfs(node.right)
        
        dfs(root)
        
        return self.res
```


