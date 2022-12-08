---
id: largest-palindromic-number
title: Largest Palindromic Number
description: Problem Description and Solution for Largest Palindromic Number
sidebar_label: 2384. Largest Palindromic Number
sidebar_position: 2384
---

# [2384. Largest Palindromic Number](https://leetcode.com/problems/largest-palindromic-number/)

```py title=largest-palindromic-number.py
class Solution:
    def largestPalindromic(self, num: str) -> str:
        counter = Counter(num)
        even = []
        odd = -1
        
        for k, v in counter.items():
            if v % 2 == 0:
                even.append((k, v))
            elif v >= 3 and v % 2 == 1:
                even.append((k, v - 1))
                odd = max(odd, int(k))
            elif v == 1:
                odd = max(odd, int(k))

        if len(even) == 1 and even[0][0] == "0":
            if odd == -1:
                return "0"
            
            return str(odd)
        
        even.sort(key = lambda x : (-int(x[0])))
        
        part = ""

        mid = "" if odd == -1 else str(odd)
        
        for k, v in even:
            part += k * (v // 2)

        return part + mid + part[::-1]
                
```


