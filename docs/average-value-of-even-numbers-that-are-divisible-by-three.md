---
id: average-value-of-even-numbers-that-are-divisible-by-three
title: Average Value of Even Numbers That Are Divisible by Three
description: Problem Description and Solution for Average Value of Even Numbers That Are Divisible by Three
sidebar_label: 2455. Average Value of Even Numbers That Are Divisible by Three
sidebar_position: 2455
---

# [2455. Average Value of Even Numbers That Are Divisible by Three](https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/)

```py title=average-value-of-even-numbers-that-are-divisible-by-three.py
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = 0
        count = 0
        
        for x in nums:
            if x % 3 == 0 and x % 2 == 0:
                res += x
                count += 1
                
        if count == 0: return 0
        
        return res // count
```


