---
id: n-ary-tree-level-order-traversal
title: N-ary Tree Level Order Traversal
description: Problem Description and Solution for N-ary Tree Level Order Traversal
sidebar_label: 429. N-ary Tree Level Order Traversal
sidebar_position: 429
---

# [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/)

```py title=n-ary-tree-level-order-traversal.py
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        res = []
        
        dq = deque([root])
        
        while dq:
            n = len(dq)
            curr = []
            
            for _ in range(n):
                node = dq.popleft()
                curr.append(node.val)
                
                for child in node.children:
                    dq.append(child)
            
            res.append(curr)
                
        return res
```


