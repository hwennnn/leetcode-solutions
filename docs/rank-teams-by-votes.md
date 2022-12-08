---
id: rank-teams-by-votes
title: Rank Teams by Votes
description: Problem Description and Solution for Rank Teams by Votes
sidebar_label: 1366. Rank Teams by Votes
sidebar_position: 1366
---

# [1366. Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)

```py title=rank-teams-by-votes.py
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        mp = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        
        for v in votes:
            for i,t in enumerate(v):
                mp[t][i] -= 1
        
        return "".join(sorted(votes[0], key = mp.get))
```


