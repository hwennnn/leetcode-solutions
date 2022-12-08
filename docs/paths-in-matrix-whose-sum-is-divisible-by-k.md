---
id: paths-in-matrix-whose-sum-is-divisible-by-k
title: Paths in Matrix Whose Sum Is Divisible by K
description: Problem Description and Solution for Paths in Matrix Whose Sum Is Divisible by K
sidebar_label: 2435. Paths in Matrix Whose Sum Is Divisible by K
sidebar_position: 2435
---

# [2435. Paths in Matrix Whose Sum Is Divisible by K](https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/)

```py title=paths-in-matrix-whose-sum-is-divisible-by-k.py
M = 10 ** 9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(rows):
            for j in range(cols):
                for kk in range(k):
                    dp[i][j][kk] %= M
                    if i + 1 < rows:
                        dp[i + 1][j][(grid[i + 1][j] + kk) % k] += dp[i][j][kk]
                    if j + 1 < cols:
                        dp[i][j + 1][(grid[i][j + 1] + kk) % k] += dp[i][j][kk]
        
        return dp[rows - 1][cols - 1][0]
```

```cpp title=paths-in-matrix-whose-sum-is-divisible-by-k.cpp
class Solution {
public:
    const long long M = 1e9 + 7;
    
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int rows = grid.size(), cols = grid[0].size();
        long long cache[rows][cols][k];
        memset(cache, -1, sizeof(cache));
        
        function<long long(int, int, int)> go = [&](int i, int j, int curr) {
            if (cache[i][j][curr] != -1) return cache[i][j][curr];
            
            if (i == rows - 1 && j == cols - 1) return (long long)(curr == 0);

            long long count = 0;

            if (i + 1 < rows) {
                count += go(i + 1, j, (curr + grid[i + 1][j]) % k);
                count %= M;
            }

            if (j + 1 < cols) {
                count += go(i, j + 1, (curr + grid[i][j + 1]) % k);
                count %= M;
            }

            return cache[i][j][curr] = count;
        };
        
        return go(0, 0, grid[0][0] % k);
    }
};
```


