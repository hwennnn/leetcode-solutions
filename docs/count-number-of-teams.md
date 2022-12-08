---
id: count-number-of-teams
title: Count Number of Teams
description: Problem Description and Solution for Count Number of Teams
sidebar_label: 1395. Count Number of Teams
sidebar_position: 1395
---

# [1395. Count Number of Teams](https://leetcode.com/problems/count-number-of-teams/)

```py title=count-number-of-teams.py
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(len(rating)):
            ls = rs = lb = rb = 0
            
            for j in range(i-1,-1,-1):
                if rating[j] < rating[i]:
                    ls += 1
                elif rating[j] > rating[i]:
                    lb += 1
            
            for j in range(i+1,len(rating)):
                if rating[j] > rating[i]:
                    rb += 1
                elif rating[j] < rating[i]:
                    rs += 1

            res += ls*rb + lb*rs
        return res
            
```


