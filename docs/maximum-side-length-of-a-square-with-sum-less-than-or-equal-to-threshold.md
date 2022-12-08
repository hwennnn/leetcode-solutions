---
id: maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold
title: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
description: Problem Description and Solution for Maximum Side Length of a Square with Sum Less than or Equal to Threshold
sidebar_label: 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold
sidebar_position: 1292
---

# [1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold](https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/)

```py title=maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold.py
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])
        prefix = [[0] * (cols+1) for _ in range(rows+1)]
        
        for i in range(1, rows+1):
            c = 0
            for j in range(1, cols + 1):
                c += mat[i-1][j-1]
                prefix[i][j] = prefix[i-1][j] + c
        
        for k in range(min(rows,cols)-1, -1, -1):
            for i in range(1, rows - k + 1):
                for j in range(1, cols - k + 1):
                    if prefix[i+k][j+k] - prefix[i-1][j+k] - prefix[i+k][j-1] + prefix[i-1][j-1] <= threshold:
                        return k+1;

        return 0
```

```java title=maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold.java
class Solution {
    public int maxSideLength(int[][] mat, int threshold) {
        int m = mat.length, n = mat[0].length;
        // Find prefix sum
        int[][] prefixSum = new int[m+1][n+1];
        for (int i = 1; i <= m; i++) {
            int sum = 0;
            for (int j = 1; j <= n; j++) {
                sum += mat[i-1][j-1];
                prefixSum[i][j] = prefixSum[i-1][j] + sum;
            }
        }
        // Start from the largest side length
        for(int k = Math.min(m, n)-1; k > 0; k--) {
            for(int i = 1; i+k <= m; i++) {
                for(int j = 1; j+k <= n; j++) {
                    if(prefixSum[i+k][j+k] - prefixSum[i-1][j+k] - prefixSum[i+k][j-1] + prefixSum[i-1][j-1] <= threshold) {
                        return k+1;
                    }
                }
            }
        }
        return 0;
    }
}
```


