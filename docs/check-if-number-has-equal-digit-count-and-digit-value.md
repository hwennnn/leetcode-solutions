---
id: check-if-number-has-equal-digit-count-and-digit-value
title: Check if Number Has Equal Digit Count and Digit Value
description: Problem Description and Solution for Check if Number Has Equal Digit Count and Digit Value
sidebar_label: 2283. Check if Number Has Equal Digit Count and Digit Value
sidebar_position: 2283
---

# [2283. Check if Number Has Equal Digit Count and Digit Value](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/)

```py title=check-if-number-has-equal-digit-count-and-digit-value.py
class Solution:
    def digitCount(self, num: str) -> bool:
        count = Counter(num)
        
        for i, x in enumerate(num):
            if count[str(i)] != int(x):
                return False
        
        return True
```


