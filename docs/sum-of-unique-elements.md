---
id: sum-of-unique-elements
title: Sum of Unique Elements
description: Problem Description and Solution for Sum of Unique Elements
sidebar_label: 1748. Sum of Unique Elements
sidebar_position: 1748
---

# [1748. Sum of Unique Elements](https://leetcode.com/problems/sum-of-unique-elements/)

```py title=sum-of-unique-elements.py
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        return sum(n for n in cnt if cnt[n] == 1)
```


