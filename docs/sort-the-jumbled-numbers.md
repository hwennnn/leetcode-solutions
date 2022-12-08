---
id: sort-the-jumbled-numbers
title: Sort the Jumbled Numbers
description: Problem Description and Solution for Sort the Jumbled Numbers
sidebar_label: 2191. Sort the Jumbled Numbers
sidebar_position: 2191
---

# [2191. Sort the Jumbled Numbers](https://leetcode.com/problems/sort-the-jumbled-numbers/)

```py title=sort-the-jumbled-numbers.py
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        res = []
        
        for index, num in enumerate(nums):
            s = str(num)
            curr = ""
            
            for char in s:
                curr += str(mapping[int(char)])
            
            res.append((int(curr), index, num))
        
        return [num for _, __, num in sorted(res)]
```


