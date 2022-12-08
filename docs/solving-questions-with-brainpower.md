---
id: solving-questions-with-brainpower
title: Solving Questions With Brainpower
description: Problem Description and Solution for Solving Questions With Brainpower
sidebar_label: 2140. Solving Questions With Brainpower
sidebar_position: 2140
---

# [2140. Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/)

```py title=solving-questions-with-brainpower.py
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        
        @cache
        def go(index):
            if index >= n: return 0
            
            points, skip = questions[index]
            
            res = go(index + 1)
            res = max(res, points + go(index + skip + 1))
            
            return res
        
        return go(0)
```


