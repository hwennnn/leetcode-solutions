---
id: longer-contiguous-segments-of-ones-than-zeros
title: Longer Contiguous Segments of Ones than Zeros
description: Problem Description and Solution for Longer Contiguous Segments of Ones than Zeros
sidebar_label: 1869. Longer Contiguous Segments of Ones than Zeros
sidebar_position: 1869
---

# [1869. Longer Contiguous Segments of Ones than Zeros](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/)

```py title=longer-contiguous-segments-of-ones-than-zeros.py
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = zeroes = 0
        
        for k, g in itertools.groupby(s):
            if k == "1":
                ones = max(ones, len(list(g)))
            else:
                zeroes = max(zeroes, len(list(g)))

        return ones > zeroes
```


