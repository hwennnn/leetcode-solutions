---
id: count-equal-and-divisible-pairs-in-an-array
title: Count Equal and Divisible Pairs in an Array
description: Problem Description and Solution for Count Equal and Divisible Pairs in an Array
sidebar_label: 2176. Count Equal and Divisible Pairs in an Array
sidebar_position: 2176
---

# [2176. Count Equal and Divisible Pairs in an Array](https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/)

```py title=count-equal-and-divisible-pairs-in-an-array.py
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        
        return res
```


