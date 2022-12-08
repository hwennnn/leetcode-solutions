---
id: remove-nth-node-from-end-of-list
title: Remove Nth Node From End of List
description: Problem Description and Solution for Remove Nth Node From End of List
sidebar_label: 19. Remove Nth Node From End of List
sidebar_position: 19
---

# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

```py title=remove-nth-node-from-end-of-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        
        for _ in range(n):
            fast = fast.next
        
        if not fast: return head.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return head
```


