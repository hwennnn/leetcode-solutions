---
id: linked-list-cycle
title: Linked List Cycle
description: Problem Description and Solution for Linked List Cycle
sidebar_label: 141. Linked List Cycle
sidebar_position: 141
---

# [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

```py title=linked-list-cycle.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
```

```cpp title=linked-list-cycle.cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        
        while (fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        
        return false;
    }
};
```


