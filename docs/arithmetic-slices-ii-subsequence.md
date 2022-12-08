---
id: arithmetic-slices-ii-subsequence
title: Arithmetic Slices II - Subsequence
description: Problem Description and Solution for Arithmetic Slices II - Subsequence
sidebar_label: 446. Arithmetic Slices II - Subsequence
sidebar_position: 446
---

# [446. Arithmetic Slices II - Subsequence](https://leetcode.com/problems/arithmetic-slices-ii-subsequence/)

```py title=arithmetic-slices-ii-subsequence.py
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [defaultdict(int) for _ in range(N)]
        res = 0

        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1

                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    res += dp[j][diff]
        
        return res
```


