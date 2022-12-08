---
id: shuffle-the-array
title: Shuffle the Array
description: Problem Description and Solution for Shuffle the Array
sidebar_label: 1470. Shuffle the Array
sidebar_position: 1470
---

# [1470. Shuffle the Array](https://leetcode.com/problems/shuffle-the-array/)

```py title=shuffle-the-array.py
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        divider = n*2//2
        first_half = nums[:divider]
        second_half = nums[divider:]
        ans = []
        
        for i in range(divider):
            ans.append(first_half[i])
            ans.append(second_half[i])

        return ans
```


