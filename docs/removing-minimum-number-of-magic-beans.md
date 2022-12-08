---
id: removing-minimum-number-of-magic-beans
title: Removing Minimum Number of Magic Beans
description: Problem Description and Solution for Removing Minimum Number of Magic Beans
sidebar_label: 2171. Removing Minimum Number of Magic Beans
sidebar_position: 2171
---

# [2171. Removing Minimum Number of Magic Beans](https://leetcode.com/problems/removing-minimum-number-of-magic-beans/)

```py title=removing-minimum-number-of-magic-beans.py
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        res = float('inf')
        n = len(beans)
        
        for i, x in enumerate(beans):
            res = min(res, total - (n - i) * x)
        
        return res
```


