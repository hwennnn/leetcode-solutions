---
id: intersection-of-two-linked-lists
title: Intersection of Two Linked Lists
description: Problem Description and Solution for Intersection of Two Linked Lists
sidebar_label: 160. Intersection of Two Linked Lists
sidebar_position: 160
---

# [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

```py title=intersection-of-two-linked-lists.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA, currB = headA, headB
        
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
            
        return currA
```

```cpp title=intersection-of-two-linked-lists.cpp
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *c1 = headA, *c2 = headB;
        
        while (c1 != c2){
            if (c1 == nullptr)
                c1 = headB;
            else
                c1 = c1->next;
            
            if (c2 == nullptr)
                c2 = headA;
            else
                c2 = c2->next;
        }
        
        return c1;
    }
};
```


