---
id: convert-the-temperature
title: Convert the Temperature
description: Problem Description and Solution for Convert the Temperature
sidebar_label: 2469. Convert the Temperature
sidebar_position: 2469
---

# [2469. Convert the Temperature](https://leetcode.com/problems/convert-the-temperature/)

```py title=convert-the-temperature.py
class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        return [c + 273.15, c * 1.80 + 32.00]
```


