---
id: valid-parentheses
title: Valid Parentheses
description: Problem Description and Solution for Valid Parentheses
sidebar_label: 20. Valid Parentheses
sidebar_position: 20
---

# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

```py title=valid-parentheses.py
class Solution:
    def isValid(self, s: str) -> bool:
        mp = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        
        for x in s:
            if x in mp:
                if not stack or stack[-1] != mp[x]:
                    return False
                stack.pop()
            else:
                stack.append(x)
        
        return len(stack) == 0
```


