---
id: check-if-all-1s-are-at-least-length-k-places-away
title: Check If All 1's Are at Least Length K Places Away
description: Problem Description and Solution for Check If All 1's Are at Least Length K Places Away
sidebar_label: 1437. Check If All 1's Are at Least Length K Places Away
sidebar_position: 1437
---

# [1437. Check If All 1's Are at Least Length K Places Away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/)

```py title=check-if-all-1s-are-at-least-length-k-places-away.py
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        stack = []
        
        for i,x in enumerate(nums):
            if x == 1:
                if stack and i - stack[-1] <= k:
                    return False
                
                stack.append(i)
        
        return True
```


