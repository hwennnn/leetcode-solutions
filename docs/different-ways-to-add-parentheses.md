---
id: different-ways-to-add-parentheses
title: Different Ways to Add Parentheses
description: Problem Description and Solution for Different Ways to Add Parentheses
sidebar_label: 241. Different Ways to Add Parentheses
sidebar_position: 241
---

# [241. Different Ways to Add Parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/)

```py title=different-ways-to-add-parentheses.py
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        N = len(expression)
        res = []

        for i, x in enumerate(expression):
            if x in "+-*":
                first = expression[:i]
                second = expression[i + 1:]

                firstPart = self.diffWaysToCompute(first)
                secondPart = self.diffWaysToCompute(second)

                for a in firstPart:
                    for b in secondPart:
                        if x == "+":
                            res.append(a + b)
                        elif x == "-":
                            res.append(a - b)
                        elif x == "*":
                            res.append(a * b)
                        
        if len(res) == 0:
            res.append(int(expression))

        return res
```


