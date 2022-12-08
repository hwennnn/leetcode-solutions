---
id: swapping-nodes-in-a-linked-list
title: Swapping Nodes in a Linked List
description: Problem Description and Solution for Swapping Nodes in a Linked List
sidebar_label: 1721. Swapping Nodes in a Linked List
sidebar_position: 1721
---

# [1721. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/)

```py title=swapping-nodes-in-a-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        res = []
        
        curr = head
        while curr:
            res.append(curr)
            curr = curr.next
        
        res[k-1].val, res[-k].val = res[-k].val, res[k-1].val
        
        return head
```


