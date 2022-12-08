---
id: min-max-game
title: Min Max Game
description: Problem Description and Solution for Min Max Game
sidebar_label: 2293. Min Max Game
sidebar_position: 2293
---

# [2293. Min Max Game](https://leetcode.com/problems/min-max-game/)

```py title=min-max-game.py
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        while len(nums) != 1:
            temp = []
            
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    temp.append(min(nums[i * 2], nums[i * 2 + 1]))
                else:
                    temp.append(max(nums[i * 2], nums[i * 2 + 1]))
            
            nums = temp
        
        return nums[0]
```


