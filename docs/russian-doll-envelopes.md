---
id: russian-doll-envelopes
title: Russian Doll Envelopes
description: Problem Description and Solution for Russian Doll Envelopes
sidebar_label: 354. Russian Doll Envelopes
sidebar_position: 354
---

# [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)

```py title=russian-doll-envelopes.py
class Solution:
    def maxEnvelopes(self, en: List[List[int]]) -> int:
        en.sort(key = lambda x: (x[0], -x[1]))
        
        nums = [j for _, j in en]
        
        def lis(nums):
            stack = []
            for x in nums:
                index = bisect_left(stack, x)
                if index == len(stack):
                    stack.append(x)
                else:
                    stack[index] = x

            return len(stack)
        
        return lis(nums)
```


