---
id: maximum-score-of-a-good-subarray
title: Maximum Score of a Good Subarray
description: Problem Description and Solution for Maximum Score of a Good Subarray
sidebar_label: 1793. Maximum Score of a Good Subarray
sidebar_position: 1793
---

# [1793. Maximum Score of a Good Subarray](https://leetcode.com/problems/maximum-score-of-a-good-subarray/)

```py title=maximum-score-of-a-good-subarray.py
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = mini = nums[k]
        i, j, n = k, k, len(nums)
        
        while i > 0 or j < n - 1:
            if (nums[i-1] if i > 0 else 0) < (nums[j + 1] if j < n - 1 else 0):
                j += 1
            else:
                i -= 1
            
            mini = min(mini, nums[i], nums[j])
            res = max(res, mini * (j - i + 1))
        
        return res
```


