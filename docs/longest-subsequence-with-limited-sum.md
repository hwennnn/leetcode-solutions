---
id: longest-subsequence-with-limited-sum
title: Longest Subsequence With Limited Sum
description: Problem Description and Solution for Longest Subsequence With Limited Sum
sidebar_label: 2389. Longest Subsequence With Limited Sum
sidebar_position: 2389
---

# [2389. Longest Subsequence With Limited Sum](https://leetcode.com/problems/longest-subsequence-with-limited-sum/)

```py title=longest-subsequence-with-limited-sum.py
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        res = []
        prefix = list(accumulate(nums, initial = 0))

        for q in queries:

            index = bisect_right(prefix, q) - 1
            res.append(index)

        return res
            
```


