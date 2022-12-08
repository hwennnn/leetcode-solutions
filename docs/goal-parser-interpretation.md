---
id: goal-parser-interpretation
title: Goal Parser Interpretation
description: Problem Description and Solution for Goal Parser Interpretation
sidebar_label: 1678. Goal Parser Interpretation
sidebar_position: 1678
---

# [1678. Goal Parser Interpretation](https://leetcode.com/problems/goal-parser-interpretation/)

```py title=goal-parser-interpretation.py
class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        
        for x in command:
            stack.append(x)
            
            if len(stack) >= 2 and stack[-2] + stack[-1] == "()":
                stack.pop()
                stack.pop()
                stack.append("o")
            elif len(stack) >= 4 and "".join(stack[-4:]) == "(al)":
                for _ in range(4):
                    stack.pop()
                stack.append("al")
        
        return "".join(stack)
```


