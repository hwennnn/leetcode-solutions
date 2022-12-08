---
id: find-the-original-array-of-prefix-xor
title: Find The Original Array of Prefix Xor
description: Problem Description and Solution for Find The Original Array of Prefix Xor
sidebar_label: 2433. Find The Original Array of Prefix Xor
sidebar_position: 2433
---

# [2433. Find The Original Array of Prefix Xor](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/)

```py title=find-the-original-array-of-prefix-xor.py
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N = len(pref)
        res = [pref[0]]

        for i in range(1, N):
            res.append(pref[i] ^ pref[i - 1])
                
        return res
```


