---
id: merge-in-between-linked-lists
title: Merge In Between Linked Lists
description: Problem Description and Solution for Merge In Between Linked Lists
sidebar_label: 1669. Merge In Between Linked Lists
sidebar_position: 1669
---

# [1669. Merge In Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists/)

```py title=merge-in-between-linked-lists.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        
        res = head = curr = ListNode()
        curr.next = list1
        
        l = -1
        
        while curr:
            if l == a:
                head = curr.next

            if l == b:
                c = list2
                while c.next:
                    c = c.next
                curr = curr.next
                while curr:
                    c.next = curr
                    curr = curr.next
                    c = c.next

                break

            curr = curr.next
            l += 1
            
        l = -1
        temp = res
        while temp and l+1 != a:
            temp = temp.next
            l += 1
        
        temp.next = list2
        
        return res.next

```

```cpp title=merge-in-between-linked-lists.cpp
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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *curr = new ListNode;
        curr->next = list1;
        ListNode *res = curr;
        
        for (int i = 0; i < a; i++)
            curr = curr->next;
        ListNode *prev = curr;
        
        for (int i = 0; i < b-a+1; i++)
            curr = curr->next;
        
        ListNode *temp = list2;
        while (temp->next)
            temp = temp->next;
        temp->next = curr->next;
        
        prev->next = list2;
        
        
        return res->next;
    }
};
```


