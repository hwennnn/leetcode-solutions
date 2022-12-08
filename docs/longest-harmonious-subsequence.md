---
id: longest-harmonious-subsequence
title: Longest Harmonious Subsequence
description: Problem Description and Solution for Longest Harmonious Subsequence
sidebar_label: 594. Longest Harmonious Subsequence
sidebar_position: 594
---

# [594. Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/)

```py title=longest-harmonious-subsequence.py
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        res = 0
        
        for num in cnt:
            if num + 1 in cnt:
                res = max(res, cnt[num] + cnt[num + 1])
        
        return res
```


