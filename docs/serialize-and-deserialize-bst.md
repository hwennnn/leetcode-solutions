---
id: serialize-and-deserialize-bst
title: Serialize and Deserialize BST
description: Problem Description and Solution for Serialize and Deserialize BST
sidebar_label: 449. Serialize and Deserialize BST
sidebar_position: 449
---

# [449. Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/)

```py title=serialize-and-deserialize-bst.py
class Codec:

    def serialize(self, root):
        vals = []

        def preOrder(node):
            if node:
                vals.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)

        return ' '.join(map(str, vals))

    # O( N ) since each val run build once
    def deserialize(self, data):
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal, val)
                node.right = build(val, maxVal)
                return node

        return build(float('-infinity'), float('infinity'))

```


