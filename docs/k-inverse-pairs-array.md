---
id: k-inverse-pairs-array
title: K Inverse Pairs Array
description: Problem Description and Solution for K Inverse Pairs Array
sidebar_label: 629. K Inverse Pairs Array
sidebar_position: 629
---

# [629. K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/)

```py title=k-inverse-pairs-array.py
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
        max_possible_inversions = (n * (n-1)//2)
        if k > max_possible_inversions:
            return 0
        if k == 0 or k == max_possible_inversions:
            return 1
        
        MOD = 10 ** 9 + 7
        
        dp = [[0]*(k+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            dp[i][0] = 1

        dp[2][1] = 1
        
        for i in range(3,n+1):
            max_possible_inversions = min(k, i*(i-1)//2)
            for j in range(1,  max_possible_inversions + 1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] 
                if j>=i:
                    dp[i][j] -= dp[i-1][j - i]
                dp[i][j] = (dp[i][j] + MOD) % MOD
            
        return dp[n][k]
```


