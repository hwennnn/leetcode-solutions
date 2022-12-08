---
id: ones-and-zeroes
title: Ones and Zeroes
description: Problem Description and Solution for Ones and Zeroes
sidebar_label: 474. Ones and Zeroes
sidebar_position: 474
---

# [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

```py title=ones-and-zeroes.py
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for s in strs:
            zeroes, ones = s.count('0'), s.count('1')
            
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeroes][j - ones] + 1)
        
        return dp[m][n]
```


