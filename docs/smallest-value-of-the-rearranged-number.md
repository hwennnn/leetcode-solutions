---
id: smallest-value-of-the-rearranged-number
title: Smallest Value of the Rearranged Number
description: Problem Description and Solution for Smallest Value of the Rearranged Number
sidebar_label: 2165. Smallest Value of the Rearranged Number
sidebar_position: 2165
---

# [2165. Smallest Value of the Rearranged Number](https://leetcode.com/problems/smallest-value-of-the-rearranged-number/)

```py title=smallest-value-of-the-rearranged-number.py
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            s = sorted(str(num))
            
            for i in range(len(s)):
                if s[i] > "0":
                    s[i], s[0] = s[0], s[i]
                    break
            
            return int("".join(s))
        else:
            num = -num
            s = sorted(str(num))
            
            return -int("".join(s[::-1]))

```


