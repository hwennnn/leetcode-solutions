---
id: search-in-a-binary-search-tree
title: Search in a Binary Search Tree
description: Problem Description and Solution for Search in a Binary Search Tree
sidebar_label: 700. Search in a Binary Search Tree
sidebar_position: 700
---

# [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

```py title=search-in-a-binary-search-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def search(node):
            if not node: return None
            
            if val == node.val:
                return node
            elif val < node.val:
                return search(node.left)
            else:
                return search(node.right)
        
        return search(root)
```


