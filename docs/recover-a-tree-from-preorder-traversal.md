---
id: recover-a-tree-from-preorder-traversal
title: Recover a Tree From Preorder Traversal
description: Problem Description and Solution for Recover a Tree From Preorder Traversal
sidebar_label: 1028. Recover a Tree From Preorder Traversal
sidebar_position: 1028
---

# [1028. Recover a Tree From Preorder Traversal](https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)

```py title=recover-a-tree-from-preorder-traversal.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, A: str) -> Optional[TreeNode]:
        stack = []
        n = len(A)
        index = 0
        
        while index < n:
            depth = 0
            
            while index < n and A[index] == '-':
                depth += 1
                index += 1
            
            val = 0
            while index < n and A[index].isdigit():
                val = val * 10 + int(A[index])
                index += 1

            while len(stack) > depth:
                stack.pop()
            
            node = TreeNode(val)
            
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)
        
        
        while len(stack) > 1:
            stack.pop()
        
        return stack.pop()
```


