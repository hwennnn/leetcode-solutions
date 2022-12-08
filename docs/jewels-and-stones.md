---
id: jewels-and-stones
title: Jewels and Stones
description: Problem Description and Solution for Jewels and Stones
sidebar_label: 771. Jewels and Stones
sidebar_position: 771
---

# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

```py title=jewels-and-stones.py
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        return sum([i in J for i in S])
```


