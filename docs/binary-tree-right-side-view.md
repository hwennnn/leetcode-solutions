---
id: binary-tree-right-side-view
title: Binary Tree Right Side View
description: Problem Description and Solution for Binary Tree Right Side View
sidebar_label: 199. Binary Tree Right Side View
sidebar_position: 199
---

# [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

```py title=binary-tree-right-side-view.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        res = []
        
        queue = deque([root])
        
        while queue:
            n = len(queue)
            count = 0
            
            for i in range(n):
                node = queue.popleft()
                
                for child in (node.left, node.right):
                    if child:
                        queue.append(child)
                    
                if i == n - 1:
                    res.append(node.val)
        
        return res
```


