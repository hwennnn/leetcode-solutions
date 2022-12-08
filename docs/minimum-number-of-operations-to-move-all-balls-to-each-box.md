---
id: minimum-number-of-operations-to-move-all-balls-to-each-box
title: Minimum Number of Operations to Move All Balls to Each Box
description: Problem Description and Solution for Minimum Number of Operations to Move All Balls to Each Box
sidebar_label: 1769. Minimum Number of Operations to Move All Balls to Each Box
sidebar_position: 1769
---

# [1769. Minimum Number of Operations to Move All Balls to Each Box](https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/)

```py title=minimum-number-of-operations-to-move-all-balls-to-each-box.py
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = []
        
        for i in range(n):
            moves = 0
            for k in range(i):
                if boxes[k] == "1":
                    moves += i - k
            
            for k in range(i+1, n):
                if boxes[k] == "1":
                    moves += k - i
            
            res.append(moves)
        
        return res
            
```


