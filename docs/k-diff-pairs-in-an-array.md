---
id: k-diff-pairs-in-an-array
title: K-diff Pairs in an Array
description: Problem Description and Solution for K-diff Pairs in an Array
sidebar_label: 532. K-diff Pairs in an Array
sidebar_position: 532
---

# [532. K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)

```py title=k-diff-pairs-in-an-array.py
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s = Counter(nums)
        res = 0
        
        for x in s:
            if k == 0 and s[x] >= 2 or k != 0 and k + x in s:
                res += 1

        return res
```


