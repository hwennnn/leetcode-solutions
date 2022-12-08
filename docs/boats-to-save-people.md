---
id: boats-to-save-people
title: Boats to Save People
description: Problem Description and Solution for Boats to Save People
sidebar_label: 881. Boats to Save People
sidebar_position: 881
---

# [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/)

```py title=boats-to-save-people.py
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        res = 0
        i, j = 0, n - 1
        
        while i <= j:
            if i != j and people[i] + people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            else:
                res += 1
                j -= 1
        
        return res
```


