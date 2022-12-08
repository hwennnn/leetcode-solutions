---
id: count-nodes-equal-to-average-of-subtree
title: Count Nodes Equal to Average of Subtree
description: Problem Description and Solution for Count Nodes Equal to Average of Subtree
sidebar_label: 2265. Count Nodes Equal to Average of Subtree
sidebar_position: 2265
---

# [2265. Count Nodes Equal to Average of Subtree](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)

```py title=count-nodes-equal-to-average-of-subtree.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            if not node: return (0, 0)
            
            lCount, lValues = go(node.left)
            rCount, rValues = go(node.right)
            
            nodeCount, nodeValues = 1 + lCount + rCount, node.val + lValues + rValues
            
            average = nodeValues // nodeCount
            
            if node.val == average:
                nonlocal res
                
                res += 1
            
            return (nodeCount, nodeValues)
        
        go(root)
        
        return res
```


