---
id: get-equal-substrings-within-budget
title: Get Equal Substrings Within Budget
description: Problem Description and Solution for Get Equal Substrings Within Budget
sidebar_label: 1208. Get Equal Substrings Within Budget
sidebar_position: 1208
---

# [1208. Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/)

```py title=get-equal-substrings-within-budget.py
class Solution:
    def equalSubstring(self, s: str, t: str, cost: int) -> int:
        i = 0
        
        for j, (a,b) in enumerate(zip(s, t)):
            cost -= abs(ord(a) - ord(b))
            
            if cost < 0:
                cost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        
        return j - i + 1
```


