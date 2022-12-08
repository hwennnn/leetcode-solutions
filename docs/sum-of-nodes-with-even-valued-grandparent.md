---
id: sum-of-nodes-with-even-valued-grandparent
title: Sum of Nodes with Even-Valued Grandparent
description: Problem Description and Solution for Sum of Nodes with Even-Valued Grandparent
sidebar_label: 1315. Sum of Nodes with Even-Valued Grandparent
sidebar_position: 1315
---

# [1315. Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/)

```py title=sum-of-nodes-with-even-valued-grandparent.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, current, parent, grandparent):
        if not current: return 0
        res = 0
        if grandparent and grandparent.val % 2 == 0:
            res += current.val
        
        return res + self.dfs(current.left, current, parent) + self.dfs(current.right, current, parent)
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.dfs(root, None, None)
```


