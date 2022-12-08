---
id: number-of-distinct-averages
title: Number of Distinct Averages
description: Problem Description and Solution for Number of Distinct Averages
sidebar_label: 2465. Number of Distinct Averages
sidebar_position: 2465
---

# [2465. Number of Distinct Averages](https://leetcode.com/problems/number-of-distinct-averages/)

```py title=number-of-distinct-averages.py
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        s = set()
        
        for i in range(N // 2):
            s.add((nums[i] + nums[~i]) / 2)
        
        return len(s)
```


