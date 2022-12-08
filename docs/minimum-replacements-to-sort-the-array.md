---
id: minimum-replacements-to-sort-the-array
title: Minimum Replacements to Sort the Array
description: Problem Description and Solution for Minimum Replacements to Sort the Array
sidebar_label: 2366. Minimum Replacements to Sort the Array
sidebar_position: 2366
---

# [2366. Minimum Replacements to Sort the Array](https://leetcode.com/problems/minimum-replacements-to-sort-the-array/)

```py title=minimum-replacements-to-sort-the-array.py
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        prev = nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] > prev:
                sections = ceil(nums[i] / prev)
                res += sections - 1
                prev = nums[i] // sections
            
            else:
                prev = nums[i]
            
        return res
```


