---
id: step-by-step-directions-from-a-binary-tree-node-to-another
title: Step-By-Step Directions From a Binary Tree Node to Another
description: Problem Description and Solution for Step-By-Step Directions From a Binary Tree Node to Another
sidebar_label: 2096. Step-By-Step Directions From a Binary Tree Node to Another
sidebar_position: 2096
---

# [2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/)

```py title=step-by-step-directions-from-a-binary-tree-node-to-another.py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        nodes = collections.defaultdict(tuple)
        
        def go(node, parent):
            if not node: return
            
            nodes[node.val] = (parent, node)
            
            go(node.left, node.val)
            go(node.right, node.val)
        
        go(root, -1)
        
        deq = collections.deque([(startValue, "")])
        visited = set([startValue])
        
        while deq:
            x, path = deq.popleft()

            if x == destValue: return path
            
            if x == -1: continue
            parent, node = nodes[x]
            
            if parent not in visited:
                visited.add(parent)
                deq.append((parent, path + "U"))
            
            if node.left and node.left.val not in visited:
                visited.add(node.left.val)
                deq.append((node.left.val, path + "L"))
            
            if node.right and node.right.val not in visited:
                visited.add(node.right.val)
                deq.append((node.right.val, path + "R"))
            
```


