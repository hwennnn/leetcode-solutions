---
id: delete-nodes-and-return-forest
title: Delete Nodes And Return Forest
description: Problem Description and Solution for Delete Nodes And Return Forest
sidebar_label: 1110. Delete Nodes And Return Forest
sidebar_position: 1110
---

# [1110. Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/)

```py title=delete-nodes-and-return-forest.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        delete = set(to_delete)
        
        def dfs(node, is_root):
            if not node: return None
            
            to_delete = node.val in delete
            
            if is_root and not to_delete:
                res.append(node)
            
            node.left = dfs(node.left, to_delete)
            node.right = dfs(node.right, to_delete)
            
            return None if to_delete else node
                        
        dfs(root, True)
        
        return res
```


