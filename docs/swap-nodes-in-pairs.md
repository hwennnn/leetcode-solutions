---
id: swap-nodes-in-pairs
title: Swap Nodes in Pairs
description: Problem Description and Solution for Swap Nodes in Pairs
sidebar_label: 24. Swap Nodes in Pairs
sidebar_position: 24
---

# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

```py title=swap-nodes-in-pairs.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = curr = ListNode(-1, head)
        
        while curr.next and curr.next.next:
            first, second = curr.next, curr.next.next
            following = curr.next.next.next
            
            curr.next, second.next, first.next = second, first, following
            
            curr = first
        
        return res.next
```


