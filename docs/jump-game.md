---
id: jump-game
title: Jump Game
description: Problem Description and Solution for Jump Game
sidebar_label: 55. Jump Game
sidebar_position: 55
---

# [55. Jump Game](https://leetcode.com/problems/jump-game/)

```py title=jump-game.py
class Solution:
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
        
```


