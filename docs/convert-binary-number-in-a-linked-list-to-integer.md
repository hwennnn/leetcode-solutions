---
id: convert-binary-number-in-a-linked-list-to-integer
title: Convert Binary Number in a Linked List to Integer
description: Problem Description and Solution for Convert Binary Number in a Linked List to Integer
sidebar_label: 1290. Convert Binary Number in a Linked List to Integer
sidebar_position: 1290
---

# [1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)

```py title=convert-binary-number-in-a-linked-list-to-integer.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        
        while head:
            res = res * 2 + head.val
            head = head.next
        
        return res
```

```cpp title=convert-binary-number-in-a-linked-list-to-integer.cpp
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
    int getDecimalValue(ListNode* head) {
        if (head == nullptr) return 0;
        int total = 0;
        
        while (head){
            total <<= 1;
            total |= head->val;
            head = head->next;
        }
        
        return total;
    }
    
};
```


