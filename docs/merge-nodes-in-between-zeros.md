---
id: merge-nodes-in-between-zeros
title: Merge Nodes in Between Zeros
description: Problem Description and Solution for Merge Nodes in Between Zeros
sidebar_label: 2181. Merge Nodes in Between Zeros
sidebar_position: 2181
---

# [2181. Merge Nodes in Between Zeros](https://leetcode.com/problems/merge-nodes-in-between-zeros/)

```py title=merge-nodes-in-between-zeros.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode(-1)
        
        s = 0
        head = head.next
        
        while head:
            if head.val == 0:
                curr.next = ListNode(s)
                curr = curr.next
                s = 0
            else:
                s += head.val
            
            head = head.next
        
        return res.next
        
```


