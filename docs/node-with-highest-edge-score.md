---
id: node-with-highest-edge-score
title: Node With Highest Edge Score
description: Problem Description and Solution for Node With Highest Edge Score
sidebar_label: 2374. Node With Highest Edge Score
sidebar_position: 2374
---

# [2374. Node With Highest Edge Score](https://leetcode.com/problems/node-with-highest-edge-score/)

```py title=node-with-highest-edge-score.py
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        scores = [0] * n
        
        for node, out in enumerate(edges):
            scores[out] += node
        
        res = maxScore = -1
        
        for node, score in enumerate(scores):
            if score > maxScore:
                maxScore = score
                res = node
        
        return res
        
```


