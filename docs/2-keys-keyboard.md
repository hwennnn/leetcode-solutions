---
id: 2-keys-keyboard
title: 2 Keys Keyboard
description: Problem Description and Solution for 2 Keys Keyboard
sidebar_label: 650. 2 Keys Keyboard
sidebar_position: 650
---

# [650. 2 Keys Keyboard](https://leetcode.com/problems/2-keys-keyboard/)

```py title=2-keys-keyboard.py
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = i
            
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break
        
        return dp[n]
```


