---
id: find-unique-binary-string
title: Find Unique Binary String
description: Problem Description and Solution for Find Unique Binary String
sidebar_label: 1980. Find Unique Binary String
sidebar_position: 1980
---

# [1980. Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/)

```py title=find-unique-binary-string.py
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        
        for i, x in enumerate(nums):
            res += "0" if x[i] == "1" else "1"
        
        return res
```


