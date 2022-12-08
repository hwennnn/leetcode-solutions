---
id: longest-arithmetic-subsequence-of-given-difference
title: Longest Arithmetic Subsequence of Given Difference
description: Problem Description and Solution for Longest Arithmetic Subsequence of Given Difference
sidebar_label: 1218. Longest Arithmetic Subsequence of Given Difference
sidebar_position: 1218
---

# [1218. Longest Arithmetic Subsequence of Given Difference](https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/)

```py title=longest-arithmetic-subsequence-of-given-difference.py
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mp = collections.defaultdict(int)
        
        for num in arr:
            mp[num] = 1 if num - difference not in mp else mp[num-difference] + 1
        
        return max(mp.values())
```


