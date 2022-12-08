---
id: count-good-nodes-in-binary-tree
title: Count Good Nodes in Binary Tree
description: Problem Description and Solution for Count Good Nodes in Binary Tree
sidebar_label: 1448. Count Good Nodes in Binary Tree
sidebar_position: 1448
---

# [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

```py title=count-good-nodes-in-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, mmax):
            if not node: return 0
            mmax = max(mmax, node.val)
            
            return (node.val >= mmax) + dfs(node.left, mmax) + dfs(node.right, mmax)
        
        return dfs(root, root.val)
```


