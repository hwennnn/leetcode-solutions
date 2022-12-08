---
id: lowest-common-ancestor-of-deepest-leaves
title: Lowest Common Ancestor of Deepest Leaves
description: Problem Description and Solution for Lowest Common Ancestor of Deepest Leaves
sidebar_label: 1123. Lowest Common Ancestor of Deepest Leaves
sidebar_position: 1123
---

# [1123. Lowest Common Ancestor of Deepest Leaves](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

```py title=lowest-common-ancestor-of-deepest-leaves.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def helper(node):
            if not node: return 0, None
            
            h1, lca1 = helper(node.left)
            h2, lca2 = helper(node.right)
            
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            
            return h1 + 1, node
        
        return helper(root)[1]
        
```


