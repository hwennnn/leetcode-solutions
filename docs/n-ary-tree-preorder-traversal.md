---
id: n-ary-tree-preorder-traversal
title: N-ary Tree Preorder Traversal
description: Problem Description and Solution for N-ary Tree Preorder Traversal
sidebar_label: 589. N-ary Tree Preorder Traversal
sidebar_position: 589
---

# [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)

```py title=n-ary-tree-preorder-traversal.py
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        
        res = []
        
        def go(node):
            res.append(node.val)
            
            for child in node.children:
                go(child)
            
        
        go(root)
        return res
```


