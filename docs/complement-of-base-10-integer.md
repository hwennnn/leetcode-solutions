---
id: complement-of-base-10-integer
title: Complement of Base 10 Integer
description: Problem Description and Solution for Complement of Base 10 Integer
sidebar_label: 1009. Complement of Base 10 Integer
sidebar_position: 1009
---

# [1009. Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/)

```py title=complement-of-base-10-integer.py
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        
        full = (1 << n.bit_length()) - 1
        
        return full ^ n
```


