---
id: generate-parentheses
title: Generate Parentheses
description: Problem Description and Solution for Generate Parentheses
sidebar_label: 22. Generate Parentheses
sidebar_position: 22
---

# [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

```py title=generate-parentheses.py
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(opened, closed, curr):
            if opened == closed == n:
                res.append(curr)
                return
            
            if closed < opened:
                backtrack(opened, closed + 1, curr + ")")
            
            if opened < n:
                backtrack(opened + 1, closed, curr + "(")
            
        backtrack(0, 0, "")
        return res
```


