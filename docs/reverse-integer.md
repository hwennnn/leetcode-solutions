---
id: reverse-integer
title: Reverse Integer
description: Problem Description and Solution for Reverse Integer
sidebar_label: 7. Reverse Integer
sidebar_position: 7
---

# [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)

```py title=reverse-integer.py
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n = cmp(x, 0) * int(str(abs(x))[::-1])
        return n if n.bit_length() < 32 else 0

```


