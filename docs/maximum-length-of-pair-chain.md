---
id: maximum-length-of-pair-chain
title: Maximum Length of Pair Chain
description: Problem Description and Solution for Maximum Length of Pair Chain
sidebar_label: 646. Maximum Length of Pair Chain
sidebar_position: 646
---

# [646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)

```py title=maximum-length-of-pair-chain.py
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        res = 1
        s, e = pairs[0]
        
        for start, end in pairs[1:]:
            if e >= start: continue
            s, e = start, end
            res += 1
        
        return res
        
```

```java title=maximum-length-of-pair-chain.java
class Solution {
    public int findLongestChain(int[][] pairs) {
        int n = pairs.length;
        if (pairs == null || n == 0) return 0;
        Arrays.sort(pairs, (a, b) -> (a[0] - b[0]));
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        
        for (int i = 0; i < n; i++){
            for (int j = 0; j < i; j++){
                dp[i] = Math.max(dp[i], pairs[i][0] > pairs[j][1] ? dp[j] + 1 : dp[j]);
            }
        }
        
        
        return dp[n-1];
    }
}
```


