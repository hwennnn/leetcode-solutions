---
id: construct-string-from-binary-tree
title: Construct String from Binary Tree
description: Problem Description and Solution for Construct String from Binary Tree
sidebar_label: 606. Construct String from Binary Tree
sidebar_position: 606
---

# [606. Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)

```py title=construct-string-from-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def go(node):
            if not node.left and not node.right:
                child = ""
            elif not node.left:
                child = "()" + go(node.right)
            elif not node.right:
                child = go(node.left)
            else:
                child = go(node.left) + go(node.right)

            return "(" + str(node.val) + child + ")"
        
        return go(root)[1: -1]
```


