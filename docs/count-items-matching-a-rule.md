---
id: count-items-matching-a-rule
title: Count Items Matching a Rule
description: Problem Description and Solution for Count Items Matching a Rule
sidebar_label: 1773. Count Items Matching a Rule
sidebar_position: 1773
---

# [1773. Count Items Matching a Rule](https://leetcode.com/problems/count-items-matching-a-rule/)

```py title=count-items-matching-a-rule.py
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        check = 0
        if ruleKey == "color": check = 1
        elif ruleKey == "name": check = 2
        
        res = 0
        for item in items:
            if item[check] == ruleValue:
                res += 1
        
        return res
        
        
```


