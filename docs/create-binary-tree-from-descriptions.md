---
id: create-binary-tree-from-descriptions
title: Create Binary Tree From Descriptions
description: Problem Description and Solution for Create Binary Tree From Descriptions
sidebar_label: 2196. Create Binary Tree From Descriptions
sidebar_position: 2196
---

# [2196. Create Binary Tree From Descriptions](https://leetcode.com/problems/create-binary-tree-from-descriptions/)

```py title=create-binary-tree-from-descriptions.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        deg = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        mp = {}
        
        for parent, child, isLeft in descriptions:
            deg[child] += 1
            
            graph[parent].append((child, isLeft))
            
        def go(parent):
            node = TreeNode(parent)
            
            for child, isLeft in graph[parent]:
                if isLeft == 1:
                    node.left = go(child)
                else:
                    node.right = go(child)
                    
            return node
            
        for parent, _, __ in descriptions:
            if deg[parent] == 0:
                return go(parent)
```


