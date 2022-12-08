---
id: generate-a-string-with-characters-that-have-odd-counts
title: Generate a String With Characters That Have Odd Counts
description: Problem Description and Solution for Generate a String With Characters That Have Odd Counts
sidebar_label: 1374. Generate a String With Characters That Have Odd Counts
sidebar_position: 1374
---

# [1374. Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/)

```py title=generate-a-string-with-characters-that-have-odd-counts.py
class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1: return "a"
        if n % 2:
            return "a"*(n-2) + "b" + "c"
        else:
            return "a"*(n-1) + "b"
```


