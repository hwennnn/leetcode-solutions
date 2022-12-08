---
id: lowest-common-ancestor-of-a-binary-search-tree
title: Lowest Common Ancestor of a Binary Search Tree
description: Problem Description and Solution for Lowest Common Ancestor of a Binary Search Tree
sidebar_label: 235. Lowest Common Ancestor of a Binary Search Tree
sidebar_position: 235
---

# [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

```py title=lowest-common-ancestor-of-a-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root):
            if root.val > p.val and root.val > q.val:
                return dfs(root.left)
            elif root.val < p.val and root.val < q.val:
                return dfs(root.right)
            else:
                return root
        
        return dfs(root)
```


