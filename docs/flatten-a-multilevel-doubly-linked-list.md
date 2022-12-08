---
id: flatten-a-multilevel-doubly-linked-list
title: Flatten a Multilevel Doubly Linked List
description: Problem Description and Solution for Flatten a Multilevel Doubly Linked List
sidebar_label: 430. Flatten a Multilevel Doubly Linked List
sidebar_position: 430
---

# [430. Flatten a Multilevel Doubly Linked List](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

```py title=flatten-a-multilevel-doubly-linked-list.py
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return
        
        dummy = Node(-1, None, head, None)
        stack = [head]
        prev = dummy
        
        while stack:
            curr = stack.pop()
            
            curr.prev = prev
            prev.next = curr
            
            if curr.next:
                stack.append(curr.next)
                curr.next = None
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
                
            prev = curr
        
        dummy.next.prev = None
        return dummy.next
```


