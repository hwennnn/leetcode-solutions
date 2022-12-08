---
id: earliest-possible-day-of-full-bloom
title: Earliest Possible Day of Full Bloom
description: Problem Description and Solution for Earliest Possible Day of Full Bloom
sidebar_label: 2136. Earliest Possible Day of Full Bloom
sidebar_position: 2136
---

# [2136. Earliest Possible Day of Full Bloom](https://leetcode.com/problems/earliest-possible-day-of-full-bloom/)

```py title=earliest-possible-day-of-full-bloom.py
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        A = sorted([(plant, grow) for plant, grow in zip(plantTime, growTime)], key = lambda x:-x[1])
        res = 0
        days = 0
        
        for plant, grow in A:
            days += plant
            res = max(res, days + grow)
        
        return res
```


