---
id: perfect-squares
title: Perfect Squares
description: Problem Description and Solution for Perfect Squares
sidebar_label: 279. Perfect Squares
sidebar_position: 279
---

# [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

```py title=perfect-squares.py
class Solution:
    def numSquares(self, N: int) -> int:
        dp = [inf] * (N + 1)
        dp[0] = 0

        for i in range(1, N + 1):
            curr = inf
            j = 1

            while i - j * j >= 0:
                k = dp[i - j * j] + 1
                if k < curr:
                    curr = k
                j += 1
            
            dp[i] = curr

        return dp[N]
```

```cpp title=perfect-squares.cpp
class Solution 
{
public:
    int numSquares(int n) 
    {
        if (n <= 0)
        {
            return 0;
        }
        
        // cntPerfectSquares[i] = the least number of perfect square numbers 
        // which sum to i. Note that cntPerfectSquares[0] is 0.
        vector<int> cntPerfectSquares(n + 1, INT_MAX);
        cntPerfectSquares[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            // For each i, it must be the sum of some number (i - j*j) and 
            // a perfect square number (j*j).
            for (int j = 1; j*j <= i; j++)
            {
                cntPerfectSquares[i] = 
                    min(cntPerfectSquares[i], cntPerfectSquares[i - j*j] + 1);
            }
        }
        
        return cntPerfectSquares.back();
    }
};
```


