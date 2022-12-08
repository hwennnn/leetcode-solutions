---
id: largest-substring-between-two-equal-characters
title: Largest Substring Between Two Equal Characters
description: Problem Description and Solution for Largest Substring Between Two Equal Characters
sidebar_label: 1624. Largest Substring Between Two Equal Characters
sidebar_position: 1624
---

# [1624. Largest Substring Between Two Equal Characters](https://leetcode.com/problems/largest-substring-between-two-equal-characters/)

```py title=largest-substring-between-two-equal-characters.py
class Solution:
    def maxLengthBetweenEqualCharacters(self, S: str) -> int:
        
        d = collections.defaultdict(list)
        
        for i, s in enumerate(S):
            d[s].append(i)

        return max(d[i][-1] - d[i][0] - 1 for i in d)
```


