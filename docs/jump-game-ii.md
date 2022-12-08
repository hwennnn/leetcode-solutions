---
id: jump-game-ii
title: Jump Game II
description: Problem Description and Solution for Jump Game II
sidebar_label: 45. Jump Game II
sidebar_position: 45
---

# [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)

```py title=jump-game-ii.py
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = currStep = currFarthest = 0
        
        for i,x in enumerate(nums[:-1]):
            currFarthest = max(currFarthest, i + x)
            
            if i == currStep:
                jumps += 1
                currStep = currFarthest
        
        return jumps
```


