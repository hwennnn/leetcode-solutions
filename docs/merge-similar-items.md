---
id: merge-similar-items
title: Merge Similar Items
description: Problem Description and Solution for Merge Similar Items
sidebar_label: 2363. Merge Similar Items
sidebar_position: 2363
---

# [2363. Merge Similar Items](https://leetcode.com/problems/merge-similar-items/)

```py title=merge-similar-items.py
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        
        for value, weight in items1 + items2:
            mp[value] += weight
        
        A = list(mp.items())
        A.sort(key = lambda x : x[0])
        
        return [[v, w] for v, w in A]
```


