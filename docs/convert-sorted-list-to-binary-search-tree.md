---
id: convert-sorted-list-to-binary-search-tree
title: Convert Sorted List to Binary Search Tree
description: Problem Description and Solution for Convert Sorted List to Binary Search Tree
sidebar_label: 109. Convert Sorted List to Binary Search Tree
sidebar_position: 109
---

# [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

```py title=convert-sorted-list-to-binary-search-tree.py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None 
        if not head.next:
            return TreeNode(head.val)
        
        pre, slow, fast = None, head, head
        
        # when fast is at the end, slow will be at mid 
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        if pre:
            # cut the parts from mid 
            pre.next = None
        
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        
        return root 
        
```


