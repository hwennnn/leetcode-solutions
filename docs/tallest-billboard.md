---
id: tallest-billboard
title: Tallest Billboard
description: Problem Description and Solution for Tallest Billboard
sidebar_label: 956. Tallest Billboard
sidebar_position: 956
---

# [956. Tallest Billboard](https://leetcode.com/problems/tallest-billboard/)

```py title=tallest-billboard.py
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = dict()
        dp[0] = 0
        
        for x in rods:
            curr = defaultdict(int)
            
            for s in dp:
                curr[s + x] = max(curr[s + x], dp[s] + x)
                curr[s] = max(curr[s], dp[s])
                curr[s - x] = max(curr[s - x], dp[s])
                
            dp = curr
        
        return dp[0]
```


