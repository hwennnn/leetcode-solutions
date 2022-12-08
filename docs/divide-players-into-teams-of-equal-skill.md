---
id: divide-players-into-teams-of-equal-skill
title: Divide Players Into Teams of Equal Skill
description: Problem Description and Solution for Divide Players Into Teams of Equal Skill
sidebar_label: 2491. Divide Players Into Teams of Equal Skill
sidebar_position: 2491
---

# [2491. Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/)

```py title=divide-players-into-teams-of-equal-skill.py
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        skill.sort()
        total = sum(skill)
        
        res = 0
        target = skill[0] + skill[-1]
        
        for i in range(N // 2):
            a, b = skill[i], skill[-i-1]
            if a + b != target: return -1
            res += a * b
        
        return res
            
```


