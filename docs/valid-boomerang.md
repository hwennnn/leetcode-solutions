---
id: valid-boomerang
title: Valid Boomerang
description: Problem Description and Solution for Valid Boomerang
sidebar_label: 1037. Valid Boomerang
sidebar_position: 1037
---

# [1037. Valid Boomerang](https://leetcode.com/problems/valid-boomerang/)

```py title=valid-boomerang.py
class Solution:
    def isBoomerang(self, p: List[List[int]]) -> bool:
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])

```


