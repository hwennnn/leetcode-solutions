---
id: remove-linked-list-elements
title: Remove Linked List Elements
description: Problem Description and Solution for Remove Linked List Elements
sidebar_label: 203. Remove Linked List Elements
sidebar_position: 203
---

# [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

```py title=remove-linked-list-elements.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        res = curr = ListNode(-1, head)
        
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            
            curr = curr.next
        
        return res.next
```

```cpp title=remove-linked-list-elements.cpp
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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *curr = new ListNode;
        curr->next = head;
        ListNode *res = curr;
        
        while (curr){
            while (curr->next && curr->next->val == val)
                curr->next = curr->next->next;
            curr = curr->next;
        }
        
        return res->next;
    }
};
```


