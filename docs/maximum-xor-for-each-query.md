---
id: maximum-xor-for-each-query
title: Maximum XOR for Each Query
description: Problem Description and Solution for Maximum XOR for Each Query
sidebar_label: 1829. Maximum XOR for Each Query
sidebar_position: 1829
---

# [1829. Maximum XOR for Each Query](https://leetcode.com/problems/maximum-xor-for-each-query/)

```py title=maximum-xor-for-each-query.py
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        m = (2 ** maximumBit) - 1
        res = []
        
        for i in range(1, n):
            nums[i] ^= nums[i - 1]

        for num in nums[::-1]:
            res.append(num ^ m)
            
        return res
```


