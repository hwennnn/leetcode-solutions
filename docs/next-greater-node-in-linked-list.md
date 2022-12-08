---
id: next-greater-node-in-linked-list
title: Next Greater Node In Linked List
description: Problem Description and Solution for Next Greater Node In Linked List
sidebar_label: 1019. Next Greater Node In Linked List
sidebar_position: 1019
---

# [1019. Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/)

```py title=next-greater-node-in-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        A = []
        
        while head:
            A.append(head.val)
            head = head.next
        
        n = len(A)
        res = [0] * n
        
        stack = []
        
        for i, x in enumerate(A):
            while stack and x > A[stack[-1]]:
                index = stack.pop()
                res[index] = x
            
            stack.append(i)
        
        return res
```


