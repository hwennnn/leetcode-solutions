---
id: maximum-swap
title: Maximum Swap
description: Problem Description and Solution for Maximum Swap
sidebar_label: 670. Maximum Swap
sidebar_position: 670
---

# [670. Maximum Swap](https://leetcode.com/problems/maximum-swap/)

```py title=maximum-swap.py
class Solution:
    def maximumSwap(self, num):
        num = list(str(num))
        mp = collections.defaultdict(int)

        for i, x in enumerate(num):
            mp[int(x)] = i
        
        for i, x in enumerate(num):
            for k in range(9, -1, -1):
                if int(x) < k and mp[k] > i:
                    num[i], num[mp[k]] = num[mp[k]], num[i]
                    return int("".join(num))
        
        return int("".join(num))
        
```


