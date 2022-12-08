---
id: guess-number-higher-or-lower
title: Guess Number Higher or Lower
description: Problem Description and Solution for Guess Number Higher or Lower
sidebar_label: 374. Guess Number Higher or Lower
sidebar_position: 374
---

# [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)

```py title=guess-number-higher-or-lower.py
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            r = guess(mid)

            if r == 0:
                return mid
            elif r == -1:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
```


