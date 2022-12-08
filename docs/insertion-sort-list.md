---
id: insertion-sort-list
title: Insertion Sort List
description: Problem Description and Solution for Insertion Sort List
sidebar_label: 147. Insertion Sort List
sidebar_position: 147
---

# [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/)

```py title=insertion-sort-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(float('-inf'))
        
        while head:
            curr = res
            while curr.next and curr.next.val < head.val:
                curr = curr.next
            curr.next = ListNode(head.val, curr.next)
            head = head.next
        
        return res.next
```


