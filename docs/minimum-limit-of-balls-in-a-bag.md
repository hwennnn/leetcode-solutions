---
id: minimum-limit-of-balls-in-a-bag
title: Minimum Limit of Balls in a Bag
description: Problem Description and Solution for Minimum Limit of Balls in a Bag
sidebar_label: 1760. Minimum Limit of Balls in a Bag
sidebar_position: 1760
---

# [1760. Minimum Limit of Balls in a Bag](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/)

```py title=minimum-limit-of-balls-in-a-bag.py
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            
            if sum((x-1) // mid for x in nums) > maxOperations:
                left = mid + 1
            else:
                right = mid
        
        return left
```


