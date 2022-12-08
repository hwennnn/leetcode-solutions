---
id: reconstruct-original-digits-from-english
title: Reconstruct Original Digits from English
description: Problem Description and Solution for Reconstruct Original Digits from English
sidebar_label: 423. Reconstruct Original Digits from English
sidebar_position: 423
---

# [423. Reconstruct Original Digits from English](https://leetcode.com/problems/reconstruct-original-digits-from-english/)

```py title=reconstruct-original-digits-from-english.py
class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = collections.Counter(s)
        digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        freq = [0] * 10
        
        for x, i in ("z", 0), ("w", 2), ("u", 4), ("x", 6), ("g", 8), ("s", 7), ("f", 5), ("o", 1),("h", 3), ("i", 9): 
            freq[i] += cnt[x]
            cnt -= Counter(digits[i]*cnt[x])
            
        return "".join(str(i)*x for i, x in enumerate(freq))

```


