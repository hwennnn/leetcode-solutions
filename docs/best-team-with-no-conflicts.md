---
id: best-team-with-no-conflicts
title: Best Team With No Conflicts
description: Problem Description and Solution for Best Team With No Conflicts
sidebar_label: 1626. Best Team With No Conflicts
sidebar_position: 1626
---

# [1626. Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/)

```py title=best-team-with-no-conflicts.py
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        players = [[a, s] for a, s in zip(ages, scores)]
        players.sort(reverse = True)
        ans = 0
        dp = [0]*n

        for i in range(n):
            score = players[i][1]
            dp[i] = score
            for j in range(i):
                if players[j][1] >= players[i][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])
        return ans
```


