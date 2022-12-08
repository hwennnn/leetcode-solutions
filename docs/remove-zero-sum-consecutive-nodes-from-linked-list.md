---
id: remove-zero-sum-consecutive-nodes-from-linked-list
title: Remove Zero Sum Consecutive Nodes from Linked List
description: Problem Description and Solution for Remove Zero Sum Consecutive Nodes from Linked List
sidebar_label: 1171. Remove Zero Sum Consecutive Nodes from Linked List
sidebar_position: 1171
---

# [1171. Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/)

```py title=remove-zero-sum-consecutive-nodes-from-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        
        prefix = 0
        head = dummy
        
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        
        return dummy.next
```


