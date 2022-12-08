---
id: total-appeal-of-a-string
title: Total Appeal of A String
description: Problem Description and Solution for Total Appeal of A String
sidebar_label: 2262. Total Appeal of A String
sidebar_position: 2262
---

# [2262. Total Appeal of A String](https://leetcode.com/problems/total-appeal-of-a-string/)

```py title=total-appeal-of-a-string.py
class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        
        def go(k):
            count = total = 0
            
            for x in s:
                if x == k:
                    total += (count * (count + 1)) // 2
                    count = 0
                else:
                    count += 1
            
            total += (count * (count + 1)) // 2
            
            return (n * (n + 1)) // 2 - total
        
        res = 0
        for k in string.ascii_lowercase:
            res += go(k)
            
        return res
```


