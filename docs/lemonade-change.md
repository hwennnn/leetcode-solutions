---
id: lemonade-change
title: Lemonade Change
description: Problem Description and Solution for Lemonade Change
sidebar_label: 860. Lemonade Change
sidebar_position: 860
---

# [860. Lemonade Change](https://leetcode.com/problems/lemonade-change/)

```py title=lemonade-change.py
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        
        for bill in bills:
            if bill == 5: five += 1
            
            elif bill == 10: five,ten = five - 1, ten + 1
                
            elif ten > 0 : five,ten = five - 1 , ten - 1
                
            else: five -= 3
                
            if five < 0: return False
            
        return True
```


