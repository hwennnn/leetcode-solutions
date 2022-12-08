---
id: remove-outermost-parentheses
title: Remove Outermost Parentheses
description: Problem Description and Solution for Remove Outermost Parentheses
sidebar_label: 1021. Remove Outermost Parentheses
sidebar_position: 1021
---

# [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)

```py title=remove-outermost-parentheses.py
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        res = []
        
        for x in s:
            if opened > 0:
                res.append(x)
                
            if x == "(":
                opened += 1
            else:
                opened -= 1
                if opened == 0:
                    res.pop()
        
        return "".join(res)
```


