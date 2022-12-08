---
id: constrained-subsequence-sum
title: Constrained Subsequence Sum
description: Problem Description and Solution for Constrained Subsequence Sum
sidebar_label: 1425. Constrained Subsequence Sum
sidebar_position: 1425
---

# [1425. Constrained Subsequence Sum](https://leetcode.com/problems/constrained-subsequence-sum/)

```py title=constrained-subsequence-sum.py
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        deq = collections.deque()
        
        for i in range(len(nums)):
            nums[i] += (0 if not deq else nums[deq[0]])
            
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            
            if nums[i] > 0:
                deq.append(i)
            
            if i >= k and deq and deq[0] == i - k:
                deq.popleft()

        
        return max(nums)
```


