---
id: check-completeness-of-a-binary-tree
title: Check Completeness of a Binary Tree
description: Problem Description and Solution for Check Completeness of a Binary Tree
sidebar_label: 958. Check Completeness of a Binary Tree
sidebar_position: 958
---

# [958. Check Completeness of a Binary Tree](https://leetcode.com/problems/check-completeness-of-a-binary-tree/)

```py title=check-completeness-of-a-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        index = 0
        
        while queue[index]:
            queue.append(queue[index].left)
            queue.append(queue[index].right)
            index += 1
        
        return all(node == None for node in queue[index:])
```


