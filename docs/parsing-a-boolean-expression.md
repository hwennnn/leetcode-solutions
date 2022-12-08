---
id: parsing-a-boolean-expression
title: Parsing A Boolean Expression
description: Problem Description and Solution for Parsing A Boolean Expression
sidebar_label: 1106. Parsing A Boolean Expression
sidebar_position: 1106
---

# [1106. Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/)

```py title=parsing-a-boolean-expression.py
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        
        for c in expression:
            if c == ")":
                seen = set()
                while stack and stack[-1] != "(":
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                stack.append(all(seen) if operator == "&" else any(seen) if operator == "|" else not seen.pop())
            elif c != ",":
                stack.append(True if c == 't' else False if c == 'f' else c)
        
        return stack.pop()
```


