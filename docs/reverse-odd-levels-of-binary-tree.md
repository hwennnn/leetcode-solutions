---
id: reverse-odd-levels-of-binary-tree
title: Reverse Odd Levels of Binary Tree
description: Problem Description and Solution for Reverse Odd Levels of Binary Tree
sidebar_label: 2415. Reverse Odd Levels of Binary Tree
sidebar_position: 2415
---

# [2415. Reverse Odd Levels of Binary Tree](https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/)

```py title=reverse-odd-levels-of-binary-tree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])
        level = 0
        
        while dq:
            n = len(dq)
            currLevel = []
            
            for _ in range(n):
                node = dq.popleft()
                currLevel.append(node)
                
                for child in filter(None, (node.left, node.right)):
                    dq.append(child)
            
            if level % 2 == 1:
                vals = [node.val for node in currLevel][::-1]
                for node, val in zip(currLevel, vals):
                    node.val = val
            
            level += 1
            
        return root
```


