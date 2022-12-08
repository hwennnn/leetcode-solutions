---
id: a-number-after-a-double-reversal
title: A Number After a Double Reversal
description: Problem Description and Solution for A Number After a Double Reversal
sidebar_label: 2119. A Number After a Double Reversal
sidebar_position: 2119
---

# [2119. A Number After a Double Reversal](https://leetcode.com/problems/a-number-after-a-double-reversal/)

```py title=a-number-after-a-double-reversal.py
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0
```


