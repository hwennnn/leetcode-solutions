---
id: most-frequent-number-following-key-in-an-array
title: Most Frequent Number Following Key In an Array
description: Problem Description and Solution for Most Frequent Number Following Key In an Array
sidebar_label: 2190. Most Frequent Number Following Key In an Array
sidebar_position: 2190
---

# [2190. Most Frequent Number Following Key In an Array](https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/)

```py title=most-frequent-number-following-key-in-an-array.py
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        count = Counter()
        
        for i, x in enumerate(nums):
            if x == key:
                if i + 1 < n:
                    count[nums[i + 1]] += 1
        
        return count.most_common()[0][0]
```


