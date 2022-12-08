---
id: minimum-operations-to-convert-number
title: Minimum Operations to Convert Number
description: Problem Description and Solution for Minimum Operations to Convert Number
sidebar_label: 2059. Minimum Operations to Convert Number
sidebar_position: 2059
---

# [2059. Minimum Operations to Convert Number](https://leetcode.com/problems/minimum-operations-to-convert-number/)

```py title=minimum-operations-to-convert-number.py
class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        queue = collections.deque([(start, 0)])
        seen = set()
        
        while queue:
            x, steps = queue.popleft()
            
            for num in nums:
                operations = [x + num, x - num, x ^ num]
                for o in operations:
                    if o == goal: return steps + 1
                    if 0 <= o <= 1000 and o not in seen:
                        queue.append((o, steps + 1))
                        seen.add(o)
        
        return -1
            
```


