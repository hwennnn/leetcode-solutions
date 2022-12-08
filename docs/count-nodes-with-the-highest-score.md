---
id: count-nodes-with-the-highest-score
title: Count Nodes With the Highest Score
description: Problem Description and Solution for Count Nodes With the Highest Score
sidebar_label: 2049. Count Nodes With the Highest Score
sidebar_position: 2049
---

# [2049. Count Nodes With the Highest Score](https://leetcode.com/problems/count-nodes-with-the-highest-score/)

```py title=count-nodes-with-the-highest-score.py
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        nodes = collections.defaultdict(list)
        freq = collections.defaultdict(int)
        
        for i, parent in enumerate(parents):
            if parent >= 0:
                nodes[parent].append(i)
        
        def go(x):
            left = right = 0
            
            if len(nodes[x]) >= 1:
                left = go(nodes[x][0])
            if len(nodes[x]) > 1:
                right = go(nodes[x][1])
            
            f = (left or 1) * (right or 1) * (len(parents) - 1 - left - right or 1)
            freq[f] += 1
            
            return 1 + left + right
        
        go(0)
        return freq[max(freq)]
        
        
```


