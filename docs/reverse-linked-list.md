---
id: reverse-linked-list
title: Reverse Linked List
description: Problem Description and Solution for Reverse Linked List
sidebar_label: 206. Reverse Linked List
sidebar_position: 206
---

# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

```py title=reverse-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
```

```cpp title=reverse-linked-list.cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *res = NULL;
        
        while (head){
            ListNode *next = head->next;
            head->next = res;
            res = head;
            head = next;
        }
        
        return res;
    }
};
```


