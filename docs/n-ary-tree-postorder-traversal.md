---
id: n-ary-tree-postorder-traversal
title: N-ary Tree Postorder Traversal
description: Problem Description and Solution for N-ary Tree Postorder Traversal
sidebar_label: 590. N-ary Tree Postorder Traversal
sidebar_position: 590
---

# [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)

```py title=n-ary-tree-postorder-traversal.py
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        temp = []
        if root == None: return temp
        def recursion(root,temp):
            for child in root.children:
                recursion(child,temp)
            
            temp.append(root.val)
            
        recursion(root,temp)
        
        return temp
            
```


