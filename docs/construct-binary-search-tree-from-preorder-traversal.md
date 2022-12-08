---
id: construct-binary-search-tree-from-preorder-traversal
title: Construct Binary Search Tree from Preorder Traversal
description: Problem Description and Solution for Construct Binary Search Tree from Preorder Traversal
sidebar_label: 1008. Construct Binary Search Tree from Preorder Traversal
sidebar_position: 1008
---

# [1008. Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

```py title=construct-binary-search-tree-from-preorder-traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def go(A, bound = float('inf')):
            if not A or A[-1] > bound: return None
            
            node = TreeNode(A.pop())
            node.left = go(A, node.val)
            node.right = go(A, bound)
            
            return node
        
        return go(preorder[::-1])
```


