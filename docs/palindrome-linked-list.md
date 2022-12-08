---
id: palindrome-linked-list
title: Palindrome Linked List
description: Problem Description and Solution for Palindrome Linked List
sidebar_label: 234. Palindrome Linked List
sidebar_position: 234
---

# [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

```py title=palindrome-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
            
        return lst == lst[::-1]
```

```cpp title=palindrome-linked-list.cpp
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
    bool isPalindrome(ListNode* head) {
        if (head == nullptr || head->next == nullptr) return true;
        
        ListNode *slow = head, *fast = head;
        
        while (fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        slow->next = reverseLL(slow->next);
        slow = slow->next;
        
        while (slow){
            if (head->val != slow->val) return false;
            
            head = head->next;
            slow = slow->next;
        }
        
        return true;
        
    }
    
    ListNode* reverseLL(ListNode *node){
        ListNode *res = NULL;
        
        while (node){
            ListNode *next = node->next;
            node->next = res;
            res = node;
            node = next;
        }
        
        return res;
    }
};
```


