---
id: maximum-matching-of-players-with-trainers
title: Maximum Matching of Players With Trainers
description: Problem Description and Solution for Maximum Matching of Players With Trainers
sidebar_label: 2410. Maximum Matching of Players With Trainers
sidebar_position: 2410
---

# [2410. Maximum Matching of Players With Trainers](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/)

```py title=maximum-matching-of-players-with-trainers.py
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        N, M = len(players), len(trainers)
        res = 0
        j = 0
        players.sort()
        trainers.sort()
        
        for player in players:
            while j < M and player > trainers[j]:
                j += 1
            
            if j == M: break
            
            j += 1
            res += 1
        
        return res
```


