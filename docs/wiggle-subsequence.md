---
id: wiggle-subsequence
title: Wiggle Subsequence
description: Problem Description and Solution for Wiggle Subsequence
sidebar_label: 376. Wiggle Subsequence
sidebar_position: 376
---

# [376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

```py title=wiggle-subsequence.py
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                down = up + 1
            elif nums[i] < nums[i - 1]:
                up = down + 1
        
        return max(up, down)
        
```


