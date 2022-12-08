---
id: largest-number-after-digit-swaps-by-parity
title: Largest Number After Digit Swaps by Parity
description: Problem Description and Solution for Largest Number After Digit Swaps by Parity
sidebar_label: 2231. Largest Number After Digit Swaps by Parity
sidebar_position: 2231
---

# [2231. Largest Number After Digit Swaps by Parity](https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/)

```py title=largest-number-after-digit-swaps-by-parity.py
class Solution:
    def largestInteger(self, num: int) -> int:
        s = list(str(num))
        n = len(s)
        odds = []
        evens = []
        oddIndex = []
        evenIndex = []
        
        for i in range(n):
            if int(s[i]) % 2 == 0:
                evens.append(s[i])
                evenIndex.append(i)
            else:
                odds.append(s[i])
                oddIndex.append(i)
                
        evens.sort(reverse = 1)
        odds.sort(reverse = 1)
        res = [None] * n
        
        for index, e in zip(evenIndex + oddIndex, evens + odds):
            res[index] = e

        return int("".join(res))
        
        
```


