---
id: largest-perimeter-triangle
title: Largest Perimeter Triangle
description: Problem Description and Solution for Largest Perimeter Triangle
sidebar_label: 976. Largest Perimeter Triangle
sidebar_position: 976
---

# [976. Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/)

```py title=largest-perimeter-triangle.py
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse = 1)
        
        for i in range(n - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
                
        return 0
```


