---
id: pairs-of-songs-with-total-durations-divisible-by-60
title: Pairs of Songs With Total Durations Divisible by 60
description: Problem Description and Solution for Pairs of Songs With Total Durations Divisible by 60
sidebar_label: 1010. Pairs of Songs With Total Durations Divisible by 60
sidebar_position: 1010
---

# [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)

```py title=pairs-of-songs-with-total-durations-divisible-by-60.py
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        s = res = 0
        mp = Counter()
        
        for x in time:
            target = (60 - x) % 60
            
            res += mp[target]
            
            mp[x % 60] += 1
        
        return res
```


