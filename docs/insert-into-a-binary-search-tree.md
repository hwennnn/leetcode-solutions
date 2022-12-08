---
id: insert-into-a-binary-search-tree
title: Insert into a Binary Search Tree
description: Problem Description and Solution for Insert into a Binary Search Tree
sidebar_label: 701. Insert into a Binary Search Tree
sidebar_position: 701
---

# [701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

```py title=insert-into-a-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: return TreeNode(val)
            
            if val > node.val:
                node.right = dfs(node.right)
            elif val < node.val:
                node.left = dfs(node.left)
        
            return node
        
        return dfs(root)
```


