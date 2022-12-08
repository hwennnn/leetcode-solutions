---
id: remove-duplicates-from-sorted-list
title: Remove Duplicates from Sorted List
description: Problem Description and Solution for Remove Duplicates from Sorted List
sidebar_label: 83. Remove Duplicates from Sorted List
sidebar_position: 83
---

# [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

```py title=remove-duplicates-from-sorted-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            
            curr = curr.next
        
        return head
```

```cpp title=remove-duplicates-from-sorted-list.cpp
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *curr = head;
        
        while (curr){
            while (curr->next && curr->val == curr->next->val){
                curr->next = curr->next->next;
            }
            curr = curr->next;
        }
        
        return head;
    }
};
```


