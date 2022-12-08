---
id: k-radius-subarray-averages
title: K Radius Subarray Averages
description: Problem Description and Solution for K Radius Subarray Averages
sidebar_label: 2090. K Radius Subarray Averages
sidebar_position: 2090
---

# [2090. K Radius Subarray Averages](https://leetcode.com/problems/k-radius-subarray-averages/)

```py title=k-radius-subarray-averages.py
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        prefix = [0] + list(accumulate(nums))
        
        for i in range(k, n - k):
            x = (prefix[i + k + 1] - prefix[i - k]) // (k + k + 1)
            res[i] = x
        
        return res
```


