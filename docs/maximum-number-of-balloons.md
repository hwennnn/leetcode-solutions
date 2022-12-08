---
id: maximum-number-of-balloons
title: Maximum Number of Balloons
description: Problem Description and Solution for Maximum Number of Balloons
sidebar_label: 1189. Maximum Number of Balloons
sidebar_position: 1189
---

# [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

```py title=maximum-number-of-balloons.py
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = collections.Counter(text)
        
        return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])
```


