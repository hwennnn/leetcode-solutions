---
id: sum-of-digits-of-string-after-convert
title: Sum of Digits of String After Convert
description: Problem Description and Solution for Sum of Digits of String After Convert
sidebar_label: 1945. Sum of Digits of String After Convert
sidebar_position: 1945
---

# [1945. Sum of Digits of String After Convert](https://leetcode.com/problems/sum-of-digits-of-string-after-convert/)

```py title=sum-of-digits-of-string-after-convert.py
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ss = ''
        
        for c in s:
            ss += str(ord(c) - ord('a') + 1)

        for _ in range(k):
            ss = str(sum(int(i) for i in ss))
            
        return int(ss)
```


