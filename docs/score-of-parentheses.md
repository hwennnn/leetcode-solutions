---
id: score-of-parentheses
title: Score of Parentheses
description: Problem Description and Solution for Score of Parentheses
sidebar_label: 856. Score of Parentheses
sidebar_position: 856
---

# [856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/)

```py title=score-of-parentheses.py
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curr = 0
        
        for x in s:
            if x == "(":
                stack.append(curr)
                curr = 0
            else:
                curr = stack.pop() + max(curr * 2, 1)
        
        return curr
```


