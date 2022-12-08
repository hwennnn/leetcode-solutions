---
id: split-array-into-consecutive-subsequences
title: Split Array into Consecutive Subsequences
description: Problem Description and Solution for Split Array into Consecutive Subsequences
sidebar_label: 659. Split Array into Consecutive Subsequences
sidebar_position: 659
---

# [659. Split Array into Consecutive Subsequences](https://leetcode.com/problems/split-array-into-consecutive-subsequences/)

```py title=split-array-into-consecutive-subsequences.py
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        once = defaultdict(int)
        twice = defaultdict(int)
        complete = defaultdict(int)
        
        for num in nums:
            if once[num - 1]:
                once[num - 1] -= 1
                twice[num] += 1
            elif twice[num - 1]:
                twice[num - 1] -= 1
                complete[num] += 1
            elif complete[num - 1]:
                complete[num - 1] -= 1
                complete[num] += 1
            else:
                once[num] += 1
        
        return sum(once.values()) + sum(twice.values()) == 0

```


