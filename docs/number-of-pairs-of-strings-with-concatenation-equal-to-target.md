---
id: number-of-pairs-of-strings-with-concatenation-equal-to-target
title: Number of Pairs of Strings With Concatenation Equal to Target
description: Problem Description and Solution for Number of Pairs of Strings With Concatenation Equal to Target
sidebar_label: 2023. Number of Pairs of Strings With Concatenation Equal to Target
sidebar_position: 2023
---

# [2023. Number of Pairs of Strings With Concatenation Equal to Target](https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/)

```py title=number-of-pairs-of-strings-with-concatenation-equal-to-target.py
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        t = len(target)
        prefix = set()
        res = 0
        
        for i in range(1, t):
            prefix.add(target[:i])
        
        for i, word1 in enumerate(nums):
            if word1 in prefix:
                for j, word2 in enumerate(nums):
                    if i != j and word1 + word2 == target:
                        res += 1
        
        return res
                
```


