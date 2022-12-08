---
id: smallest-subtree-with-all-the-deepest-nodes
title: Smallest Subtree with all the Deepest Nodes
description: Problem Description and Solution for Smallest Subtree with all the Deepest Nodes
sidebar_label: 865. Smallest Subtree with all the Deepest Nodes
sidebar_position: 865
---

# [865. Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

```py title=smallest-subtree-with-all-the-deepest-nodes.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, depth):
            if not node: return node, depth
            
            left, leftDepth = dfs(node.left, depth+1)
            right, rightDepth = dfs(node.right, depth+1)
            
            if leftDepth > rightDepth: return left, leftDepth
            
            if rightDepth > leftDepth: return right, rightDepth
            
            return node, leftDepth
        
        return dfs(root,0)[0]
```


