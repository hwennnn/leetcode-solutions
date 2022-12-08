---
id: path-in-zigzag-labelled-binary-tree
title: Path In Zigzag Labelled Binary Tree
description: Problem Description and Solution for Path In Zigzag Labelled Binary Tree
sidebar_label: 1104. Path In Zigzag Labelled Binary Tree
sidebar_position: 1104
---

# [1104. Path In Zigzag Labelled Binary Tree](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)

```py title=path-in-zigzag-labelled-binary-tree.py
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        level = nodes = 1
        
        while label >= nodes * 2:
            nodes *= 2
            level += 1
        
        while label != 0:
            res.append(label)
            mmax = (2 ** level) - 1
            mmin = 2 ** (level - 1)
            label = (mmax + mmin - label) // 2
            level -= 1
        
        return res[::-1]
```


