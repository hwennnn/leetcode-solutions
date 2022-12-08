---
id: count-complete-tree-nodes
title: Count Complete Tree Nodes
description: Problem Description and Solution for Count Complete Tree Nodes
sidebar_label: 222. Count Complete Tree Nodes
sidebar_position: 222
---

# [222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

```py title=count-complete-tree-nodes.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def countDepth(node, countLeft = True):
            depth = 0
            
            while node:
                depth += 1
                if countLeft:
                    node = node.left
                else:
                    node = node.right
            
            return depth
        
        left, right = countDepth(root), countDepth(root, False)
        
        if left == right:
            return (1 << left) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```


