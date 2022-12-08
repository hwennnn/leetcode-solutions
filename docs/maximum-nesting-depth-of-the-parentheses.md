---
id: maximum-nesting-depth-of-the-parentheses
title: Maximum Nesting Depth of the Parentheses
description: Problem Description and Solution for Maximum Nesting Depth of the Parentheses
sidebar_label: 1614. Maximum Nesting Depth of the Parentheses
sidebar_position: 1614
---

# [1614. Maximum Nesting Depth of the Parentheses](https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/)

```py title=maximum-nesting-depth-of-the-parentheses.py
class Solution:
    def maxDepth(self, S: str) -> int:
        depth = 0
        res = 0
        
        for s in S:
            if s == "(":
                depth += 1
            elif s == ")":
                depth -= 1
            
            res = max(res, depth)
        
        return res
```


