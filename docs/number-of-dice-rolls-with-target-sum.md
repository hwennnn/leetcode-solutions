---
id: number-of-dice-rolls-with-target-sum
title: Number of Dice Rolls With Target Sum
description: Problem Description and Solution for Number of Dice Rolls With Target Sum
sidebar_label: 1155. Number of Dice Rolls With Target Sum
sidebar_position: 1155
---

# [1155. Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)

```py title=number-of-dice-rolls-with-target-sum.py
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def go(dices, total):
            if dices == 0:
                return int(total == target)
            
            count = 0
            
            for x in range(1, k + 1):
                if x + total > target: break
                
                count += go(dices - 1, x + total)
                count %= M
            
            return count 
        
        return go(n, 0)
                
        
```


