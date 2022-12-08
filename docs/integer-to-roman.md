---
id: integer-to-roman
title: Integer to Roman
description: Problem Description and Solution for Integer to Roman
sidebar_label: 12. Integer to Roman
sidebar_position: 12
---

# [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)

```py title=integer-to-roman.py
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        mp = [("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50), ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)]

        for symbol, x in mp[::-1]:
            if num >= x:
                res += symbol * (num // x)
                num %= x
        
        return res
```


