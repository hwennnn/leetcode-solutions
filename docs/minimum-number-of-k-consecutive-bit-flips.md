---
id: minimum-number-of-k-consecutive-bit-flips
title: Minimum Number of K Consecutive Bit Flips
description: Problem Description and Solution for Minimum Number of K Consecutive Bit Flips
sidebar_label: 995. Minimum Number of K Consecutive Bit Flips
sidebar_position: 995
---

# [995. Minimum Number of K Consecutive Bit Flips](https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/)

```py title=minimum-number-of-k-consecutive-bit-flips.py
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        queue = deque()
        res = 0
        
        for i, x in enumerate(nums):
            if x == 0:
                if len(queue) % 2 == 0:
                    res += 1
                    queue.append(i + k - 1)
            else:
                if len(queue) & 1:
                    res += 1
                    queue.append(i + k - 1)
            
            if queue and i >= queue[0]:
                queue.popleft()
        
        return res if len(queue) == 0 else -1
```


