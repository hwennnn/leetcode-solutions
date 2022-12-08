---
id: subarray-sums-divisible-by-k
title: Subarray Sums Divisible by K
description: Problem Description and Solution for Subarray Sums Divisible by K
sidebar_label: 974. Subarray Sums Divisible by K
sidebar_position: 974
---

# [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)

```py title=subarray-sums-divisible-by-k.py
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(int)
        mp[0] = 1
        res = s = 0
        
        for x in nums:
            s = (s + x) % k
            
            res += mp[s]
            
            mp[s] += 1
            
        return res
```


