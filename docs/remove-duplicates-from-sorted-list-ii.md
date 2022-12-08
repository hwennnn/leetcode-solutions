---
id: remove-duplicates-from-sorted-list-ii
title: Remove Duplicates from Sorted List II
description: Problem Description and Solution for Remove Duplicates from Sorted List II
sidebar_label: 82. Remove Duplicates from Sorted List II
sidebar_position: 82
---

# [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

```py title=remove-duplicates-from-sorted-list-ii.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode(-1, head)
        
        while curr:
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                v = curr.next.val
                p = curr.next
                
                while p and p.val == v:
                    p = p.next
                
                curr.next = p
            else:
                curr = curr.next
        
        return res.next
```


