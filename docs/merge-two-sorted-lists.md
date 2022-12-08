---
id: merge-two-sorted-lists
title: Merge Two Sorted Lists
description: Problem Description and Solution for Merge Two Sorted Lists
sidebar_label: 21. Merge Two Sorted Lists
sidebar_position: 21
---

# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

```py title=merge-two-sorted-lists.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode(-1)
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        
        rem = list1 or list2
        curr.next = rem
        
        return res.next
```

```cpp title=merge-two-sorted-lists.cpp
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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *curr = new ListNode;
        curr->val = -1;
        curr->next = NULL;
        ListNode *res = curr;
        
        while (l1 != nullptr && l2 != nullptr){
            if (l1->val < l2->val){
                curr->next = l1;
                l1 = l1->next;
            }else{
                curr->next = l2;
                l2 = l2->next;
            }
            
            curr = curr->next;
        }
        
        ListNode *leftover = (l1 == nullptr) ? l2 : l1;
        curr->next = leftover;
        
        return res->next;
    }
};
```


