---
id: minimum-number-of-buckets-required-to-collect-rainwater-from-houses
title: Minimum Number of Buckets Required to Collect Rainwater from Houses
description: Problem Description and Solution for Minimum Number of Buckets Required to Collect Rainwater from Houses
sidebar_label: 2086. Minimum Number of Buckets Required to Collect Rainwater from Houses
sidebar_position: 2086
---

# [2086. Minimum Number of Buckets Required to Collect Rainwater from Houses](https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/)

```py title=minimum-number-of-buckets-required-to-collect-rainwater-from-houses.py
class Solution:
    def minimumBuckets(self, s: str) -> int:
        s = list(s)
        n = len(s)
        
        for i, x in enumerate(s):
            if x != "H": continue
            if i - 1 >= 0 and s[i - 1] == "B": continue
                
            if i + 1 < n and s[i + 1] == ".":
                s[i + 1] = "B"
            elif i - 1 >= 0 and s[i - 1] == ".":
                s[i - 1] = "B"
            else:
                return -1
            
        return s.count("B")
```


