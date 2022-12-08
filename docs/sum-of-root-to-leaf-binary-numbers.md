---
id: sum-of-root-to-leaf-binary-numbers
title: Sum of Root To Leaf Binary Numbers
description: Problem Description and Solution for Sum of Root To Leaf Binary Numbers
sidebar_label: 1022. Sum of Root To Leaf Binary Numbers
sidebar_position: 1022
---

# [1022. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)

```py title=sum-of-root-to-leaf-binary-numbers.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node, curr):
            nonlocal res
            
            if not node: return
            
            v = curr * 2 + node.val
            
            if not node.left and not node.right:
                res += v
                return
            
            go(node.left, v)
            go(node.right, v)
        
        go(root, 0)
        
        return res
```


