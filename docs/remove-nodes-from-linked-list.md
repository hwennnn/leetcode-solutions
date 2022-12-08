---
id: remove-nodes-from-linked-list
title: Remove Nodes From Linked List
description: Problem Description and Solution for Remove Nodes From Linked List
sidebar_label: 2487. Remove Nodes From Linked List
sidebar_position: 2487
---

# [2487. Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list/)

```py title=remove-nodes-from-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head
        
        while curr:
            while stack and curr.val > stack[-1]:
                stack.pop()
                
            stack.append(curr.val)
            curr = curr.next

        curr = res = ListNode(-1)
        
        for x in stack:
            curr.next = ListNode(x)
            curr = curr.next
        
        return res.next
```


