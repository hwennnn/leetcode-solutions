---
id: most-beautiful-item-for-each-query
title: Most Beautiful Item for Each Query
description: Problem Description and Solution for Most Beautiful Item for Each Query
sidebar_label: 2070. Most Beautiful Item for Each Query
sidebar_position: 2070
---

# [2070. Most Beautiful Item for Each Query](https://leetcode.com/problems/most-beautiful-item-for-each-query/)

```py title=most-beautiful-item-for-each-query.py
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        items.sort(key = lambda x : (x[0], -x[1]))
        res = []
        A = [(0, 0)]
        curr = 0

        for i, (price, beauty) in enumerate(items):
            if i > 1 and price == items[i - 1][0]: continue
                
            curr = max(curr, beauty)
            A.append((price, curr))

        for q in queries:
            index = bisect.bisect(A, (q + 1, )) - 1
            res.append(A[index][1])
            
        return res
            
```


