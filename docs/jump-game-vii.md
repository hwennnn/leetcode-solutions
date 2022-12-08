---
id: jump-game-vii
title: Jump Game VII
description: Problem Description and Solution for Jump Game VII
sidebar_label: 1871. Jump Game VII
sidebar_position: 1871
---

# [1871. Jump Game VII](https://leetcode.com/problems/jump-game-vii/)

```py title=jump-game-vii.py
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [c == "0" for c in s]
        m = 0
        
        for i in range(1, len(s)):
            if i >= minJump: m += dp[i - minJump]
            if i > maxJump: m -= dp[i - maxJump - 1]
            
            dp[i] &= m > 0
        
        return dp[-1]
```


