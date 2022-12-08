---
id: count-number-of-nice-subarrays
title: Count Number of Nice Subarrays
description: Problem Description and Solution for Count Number of Nice Subarrays
sidebar_label: 1248. Count Number of Nice Subarrays
sidebar_position: 1248
---

# [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/)

```py title=count-number-of-nice-subarrays.py
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = i = count = 0
        
        for j,x in enumerate(nums):
            if x & 1:
                k -= 1
                count = 0
            
            while k == 0:
                k += nums[i] & 1
                i += 1
                count += 1
            
            res += count

        return res
```


