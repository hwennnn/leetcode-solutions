---
id: largest-number-after-mutating-substring
title: Largest Number After Mutating Substring
description: Problem Description and Solution for Largest Number After Mutating Substring
sidebar_label: 1946. Largest Number After Mutating Substring
sidebar_position: 1946
---

# [1946. Largest Number After Mutating Substring](https://leetcode.com/problems/largest-number-after-mutating-substring/)

```py title=largest-number-after-mutating-substring.py
class Solution:
    def maximumNumber(self, nums: str, change: List[int]) -> str:
        nums = list(nums)
        done = False
        
        for i, num in enumerate(nums):
            pos = int(num)
            if change[pos] >= pos:
                nums[i] = str(change[pos])
                if change[pos] > pos:
                    done = True
            else:
                if done:
                    break
        
        return "".join(nums)
```


