---
id: broken-calculator
title: Broken Calculator
description: Problem Description and Solution for Broken Calculator
sidebar_label: 991. Broken Calculator
sidebar_position: 991
---

# [991. Broken Calculator](https://leetcode.com/problems/broken-calculator/)

```py title=broken-calculator.py
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue == target: return 0
        if startValue > target: return startValue - target
        
        if target % 2 == 0:
            return self.brokenCalc(startValue, target // 2) + 1
        else:
            return self.brokenCalc(startValue, target + 1) + 1
```


