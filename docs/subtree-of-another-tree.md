---
id: subtree-of-another-tree
title: Subtree of Another Tree
description: Problem Description and Solution for Subtree of Another Tree
sidebar_label: 572. Subtree of Another Tree
sidebar_position: 572
---

# [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

```py title=subtree-of-another-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        
        def isSameTree(a, b):
            if not a and not b: return True
            if not a or not b: return False
            
            return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
        
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
```


