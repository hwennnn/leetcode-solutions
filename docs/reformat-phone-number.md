---
id: reformat-phone-number
title: Reformat Phone Number
description: Problem Description and Solution for Reformat Phone Number
sidebar_label: 1694. Reformat Phone Number
sidebar_position: 1694
---

# [1694. Reformat Phone Number](https://leetcode.com/problems/reformat-phone-number/)

```py title=reformat-phone-number.py
class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-","").replace(" ", "")

        n = len(number)
        i = 0
        res = []
        while n > 4:
            res.append(number[i:i+3])
            i += 3
            n -= 3
        
        if n == 4:
            res.append(number[i:i+2])
            res.append(number[i+2:i+4])
        else:
            res.append(number[i:])
        
        return "-".join(res)
```


