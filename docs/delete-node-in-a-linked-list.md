---
id: delete-node-in-a-linked-list
title: Delete Node in a Linked List
description: Problem Description and Solution for Delete Node in a Linked List
sidebar_label: 237. Delete Node in a Linked List
sidebar_position: 237
---

# [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

```py title=delete-node-in-a-linked-list.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        node.val , node.next = node.next.val, node.next.next
```

```cpp title=delete-node-in-a-linked-list.cpp
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
    void deleteNode(ListNode* node) {
        *node = *node->next;
    }
};
```


