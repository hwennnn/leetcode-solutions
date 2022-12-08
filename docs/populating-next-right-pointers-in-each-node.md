---
id: populating-next-right-pointers-in-each-node
title: Populating Next Right Pointers in Each Node
description: Problem Description and Solution for Populating Next Right Pointers in Each Node
sidebar_label: 116. Populating Next Right Pointers in Each Node
sidebar_position: 116
---

# [116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)

```py title=populating-next-right-pointers-in-each-node.py
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.left and node.right:
                node.left.next = node.right
                
                if node.next:
                    node.right.next = node.next.left
                
                queue.append(node.left)
                queue.append(node.right)
        
        return root
```


