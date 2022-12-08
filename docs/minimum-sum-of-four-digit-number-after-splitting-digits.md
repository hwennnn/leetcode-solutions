---
id: minimum-sum-of-four-digit-number-after-splitting-digits
title: Minimum Sum of Four Digit Number After Splitting Digits
description: Problem Description and Solution for Minimum Sum of Four Digit Number After Splitting Digits
sidebar_label: 2160. Minimum Sum of Four Digit Number After Splitting Digits
sidebar_position: 2160
---

# [2160. Minimum Sum of Four Digit Number After Splitting Digits](https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/)

```py title=minimum-sum-of-four-digit-number-after-splitting-digits.py
class Solution:
    def minimumSum(self, num: int) -> int:
        digits = [int(c) for c in str(num)]
        digits.sort()
        return (digits[0] * 10 + digits[2]) + (digits[1] * 10 + digits[3])
```


