---
id: beautiful-arrangement
title: Beautiful Arrangement
description: Problem Description and Solution for Beautiful Arrangement
sidebar_label: 526. Beautiful Arrangement
sidebar_position: 526
---

# [526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/)

```py title=beautiful-arrangement.py
class Solution:
    def countArrangement(self, n: int) -> int:
        
        def dfs(count, used):
            if count == 0: return 1
            
            res = 0
            for i in range(1, n+1):
                if not used[i] and (not i%count or not count%i):
                    used[i] = True
                    res += dfs(count-1, used)
                    used[i] = False
            
            return res
        
        return dfs(n, [False]*(n+1))
```


