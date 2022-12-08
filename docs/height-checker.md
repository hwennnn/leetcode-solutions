---
id: height-checker
title: Height Checker
description: Problem Description and Solution for Height Checker
sidebar_label: 1051. Height Checker
sidebar_position: 1051
---

# [1051. Height Checker](https://leetcode.com/problems/height-checker/)

```py title=height-checker.py
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        
        for a,b in zip(heights, sorted(heights)):
            res += int(a != b)
        
        return res
```


