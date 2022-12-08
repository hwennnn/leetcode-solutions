---
id: odd-even-linked-list
title: Odd Even Linked List
description: Problem Description and Solution for Odd Even Linked List
sidebar_label: 328. Odd Even Linked List
sidebar_position: 328
---

# [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

```py title=odd-even-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        o = odd = ListNode(-1)
        e = even = ListNode(-1)
        
        isOdd = True
        while head:
            node = ListNode(head.val)
            if isOdd:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            
            isOdd = not isOdd
            head = head.next
        
        odd.next = e.next
        
        return o.next
```


