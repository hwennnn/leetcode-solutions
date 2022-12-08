---
id: find-players-with-zero-or-one-losses
title: Find Players With Zero or One Losses
description: Problem Description and Solution for Find Players With Zero or One Losses
sidebar_label: 2225. Find Players With Zero or One Losses
sidebar_position: 2225
---

# [2225. Find Players With Zero or One Losses](https://leetcode.com/problems/find-players-with-zero-or-one-losses/)

```py title=find-players-with-zero-or-one-losses.py
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        res = [[] for _ in range(2)]

        for winner, loser in matches:
            if winner not in loses:
                loses[winner] = 0
            
            if loser not in loses:
                loses[loser] = 1
            else:
                loses[loser] += 1

        for player, loseCount in loses.items():
            if loseCount == 0:
                res[0].append(player)
            elif loseCount == 1:
                res[1].append(player)

        res[0].sort()
        res[1].sort()

        return res
```


