---
id: kids-with-the-greatest-number-of-candies
title: Kids With the Greatest Number of Candies
description: Problem Description and Solution for Kids With the Greatest Number of Candies
sidebar_label: 1431. Kids With the Greatest Number of Candies
sidebar_position: 1431
---

# [1431. Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)

```py title=kids-with-the-greatest-number-of-candies.py
class Solution:
    def kidsWithCandies(self, candies: List[int], ec: int) -> List[bool]:
        m = max(candies)
        
        res = []
        
        for i, c in enumerate(candies):
            res.append(c+ec >= m)
        
        return res
            
```


