---
id: linked-list-cycle-ii
title: Linked List Cycle II
description: Problem Description and Solution for Linked List Cycle II
sidebar_label: 142. Linked List Cycle II
sidebar_position: 142
---

# [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

```py title=linked-list-cycle-ii.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                while slow != head:
                    slow = slow.next
                    head = head.next
                
                return head
        
        return None
```


