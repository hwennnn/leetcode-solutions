---
id: next-greater-element-iv
title: Next Greater Element IV
description: Problem Description and Solution for Next Greater Element IV
sidebar_label: 2454. Next Greater Element IV
sidebar_position: 2454
---

# [2454. Next Greater Element IV](https://leetcode.com/problems/next-greater-element-iv/)

```py title=next-greater-element-iv.py
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N
        stack = []
        pq = []
        
        for i, x in enumerate(nums):
            while pq and x > pq[0][0]:
                rx, ri = heappop(pq)
                res[ri] = x

            while stack and x > nums[stack[-1]]:
                popIndex = stack.pop()
                heappush(pq, (nums[popIndex], popIndex))
            
            stack.append(i)

        return res
```


