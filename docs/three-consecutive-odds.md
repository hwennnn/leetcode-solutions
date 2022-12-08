---
id: three-consecutive-odds
title: Three Consecutive Odds
description: Problem Description and Solution for Three Consecutive Odds
sidebar_label: 1550. Three Consecutive Odds
sidebar_position: 1550
---

# [1550. Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds/)

```py title=three-consecutive-odds.py
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        
        for num in arr:
            if num % 2 == 1:
                count += 1
            else:
                count = 0
            
            if count == 3:
                return True
        
        return count == 3
```


