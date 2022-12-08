---
id: range-sum-query-immutable
title: Range Sum Query - Immutable
description: Problem Description and Solution for Range Sum Query - Immutable
sidebar_label: 303. Range Sum Query - Immutable
sidebar_position: 303
---

# [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

```py title=range-sum-query-immutable.py
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] + list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```


