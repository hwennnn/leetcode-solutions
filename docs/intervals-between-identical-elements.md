---
id: intervals-between-identical-elements
title: Intervals Between Identical Elements
description: Problem Description and Solution for Intervals Between Identical Elements
sidebar_label: 2121. Intervals Between Identical Elements
sidebar_position: 2121
---

# [2121. Intervals Between Identical Elements](https://leetcode.com/problems/intervals-between-identical-elements/)

```py title=intervals-between-identical-elements.py
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        res = []
        mp = collections.defaultdict(list)
        prefix = collections.defaultdict(list)
        
        for i, x in enumerate(arr):
            mp[x].append(i)
            prefix[x].append(i)
        
        for k, p in prefix.items():
            for i in range(1, len(p)):
                p[i] += p[i - 1]
            prefix[k] = [0] + prefix[k]
        
        for i, x in enumerate(arr):
            n = len(mp[x])
              
            index = bisect.bisect_left(mp[x], i)

            left = index * i - (prefix[x][index] - prefix[x][0])
            right = (prefix[x][-1] - prefix[x][index + 1]) - i * (n - index - 1)

            res.append(left + right)
        
        return res
        
```


