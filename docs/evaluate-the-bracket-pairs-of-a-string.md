---
id: evaluate-the-bracket-pairs-of-a-string
title: Evaluate the Bracket Pairs of a String
description: Problem Description and Solution for Evaluate the Bracket Pairs of a String
sidebar_label: 1807. Evaluate the Bracket Pairs of a String
sidebar_position: 1807
---

# [1807. Evaluate the Bracket Pairs of a String](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/)

```py title=evaluate-the-bracket-pairs-of-a-string.py
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        mp = {k:v for k,v in knowledge}
        res = []
        key = ""
        going = False
        
        for i,x in enumerate(s):
            if x == "(":
                going = True
            elif x == ")":
                going = False
                res.append(mp.get(key, "?"))
                key = ""
            elif going:
                key += x
            else:
                res.append(x)
        
        return "".join(res)
```


