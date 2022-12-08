---
id: count-nice-pairs-in-an-array
title: Count Nice Pairs in an Array
description: Problem Description and Solution for Count Nice Pairs in an Array
sidebar_label: 1814. Count Nice Pairs in an Array
sidebar_position: 1814
---

# [1814. Count Nice Pairs in an Array](https://leetcode.com/problems/count-nice-pairs-in-an-array/)

```py title=count-nice-pairs-in-an-array.py
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = Counter(num - int(str(num)[::-1]) for num in nums)
        
        return sum((c * (c-1) // 2) for c in count.values()) % (10 ** 9 + 7)
```


