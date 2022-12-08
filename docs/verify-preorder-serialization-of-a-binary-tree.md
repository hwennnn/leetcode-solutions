---
id: verify-preorder-serialization-of-a-binary-tree
title: Verify Preorder Serialization of a Binary Tree
description: Problem Description and Solution for Verify Preorder Serialization of a Binary Tree
sidebar_label: 331. Verify Preorder Serialization of a Binary Tree
sidebar_position: 331
---

# [331. Verify Preorder Serialization of a Binary Tree](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)

```py title=verify-preorder-serialization-of-a-binary-tree.py
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        diff = 1
        
        for node in preorder:
            diff -= 1
            if diff < 0: return False
            if node != '#':
                diff += 2
        
        return diff == 0
```


