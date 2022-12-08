---
id: delete-the-middle-node-of-a-linked-list
title: Delete the Middle Node of a Linked List
description: Problem Description and Solution for Delete the Middle Node of a Linked List
sidebar_label: 2095. Delete the Middle Node of a Linked List
sidebar_position: 2095
---

# [2095. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)

```py title=delete-the-middle-node-of-a-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = slow = fast = ListNode(-1, head)
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        
        return res.next
```


