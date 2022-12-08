---
id: count-of-matches-in-tournament
title: Count of Matches in Tournament
description: Problem Description and Solution for Count of Matches in Tournament
sidebar_label: 1688. Count of Matches in Tournament
sidebar_position: 1688
---

# [1688. Count of Matches in Tournament](https://leetcode.com/problems/count-of-matches-in-tournament/)

```py title=count-of-matches-in-tournament.py
class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        
        while n > 1:
            if n%2:
                res += int((n-1) / 2)
                n = int((n-1) / 2 + 1)
            else:
                res += n//2
                n //= 2
        
        return res
```


