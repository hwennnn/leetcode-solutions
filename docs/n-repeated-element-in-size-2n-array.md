---
id: n-repeated-element-in-size-2n-array
title: N-Repeated Element in Size 2N Array
description: Problem Description and Solution for N-Repeated Element in Size 2N Array
sidebar_label: 961. N-Repeated Element in Size 2N Array
sidebar_position: 961
---

# [961. N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

```py title=n-repeated-element-in-size-2n-array.py
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 2
        
        count = Counter(nums)
        
        for k, v in count.items():
            if v == n:
                return k
```


