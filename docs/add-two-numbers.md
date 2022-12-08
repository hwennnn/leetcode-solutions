---
id: add-two-numbers
title: Add Two Numbers
description: Problem Description and Solution for Add Two Numbers
sidebar_label: 2. Add Two Numbers
sidebar_position: 2
---

# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

```py title=add-two-numbers.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = res = ListNode(-1)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next
            
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        
        return res.next
```

```cpp title=add-two-numbers.cpp
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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode res(-1), *curr = &res;
        
        int carry = 0;
        
        while (l1 || l2 || carry > 0){
            if (l1){
                carry += l1->val;
                l1 = l1->next;
            }
            
            if (l2){
                carry += l2->val;
                l2 = l2->next;
            }
            
            curr->next = new ListNode(carry%10);
            curr = curr->next;
            
            carry /= 10;
                
        }
        
        return res.next;
    }
};
```


