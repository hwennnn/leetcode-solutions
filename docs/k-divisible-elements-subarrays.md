---
id: k-divisible-elements-subarrays
title: K Divisible Elements Subarrays
description: Problem Description and Solution for K Divisible Elements Subarrays
sidebar_label: 2261. K Divisible Elements Subarrays
sidebar_position: 2261
---

# [2261. K Divisible Elements Subarrays](https://leetcode.com/problems/k-divisible-elements-subarrays/)

```py title=k-divisible-elements-subarrays.py
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        BASE, MOD = 401, 8390190857
        n = len(nums)
        h = [1]
        seen = set()
        
        for _ in range(n):
            h.append((h[-1] * BASE) % MOD)
        
        for sz in range(1, n + 1):
            curr = 0
            count = 0
            
            for i in range(sz):
                curr = (curr * BASE) + nums[i]
                curr %= MOD
                
                if nums[i] % p == 0:
                    count += 1
            
            if count <= k:
                seen.add(curr)
            
            for i in range(sz, n):
                if nums[i] % p == 0:
                    count += 1
                
                if nums[i - sz] % p == 0:
                    count -= 1
                
                curr = (curr * BASE) + nums[i]
                curr %= MOD
                curr -= nums[i - sz] * h[sz]
                curr %= MOD
                
                if count <= k:
                    seen.add(curr)
            
        return len(seen)
        
        
        
```


