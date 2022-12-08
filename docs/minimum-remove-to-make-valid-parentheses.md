---
id: minimum-remove-to-make-valid-parentheses
title: Minimum Remove to Make Valid Parentheses
description: Problem Description and Solution for Minimum Remove to Make Valid Parentheses
sidebar_label: 1249. Minimum Remove to Make Valid Parentheses
sidebar_position: 1249
---

# [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)

```py title=minimum-remove-to-make-valid-parentheses.py
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        stack = []
        res = [""] * n
        
        for i, x in enumerate(s):
            if x == "(":
                stack.append((x, i))
            elif x == ")":
                if stack and stack[-1][0] == "(":
                    ele, index = stack.pop()
                    res[index] = ele
                    res[i] = x
                else:
                    if stack:
                        stack.pop()
            else:
                res[i] = x
        
        return "".join(res)
```


