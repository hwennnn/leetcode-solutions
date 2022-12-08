---
id: reverse-substrings-between-each-pair-of-parentheses
title: Reverse Substrings Between Each Pair of Parentheses
description: Problem Description and Solution for Reverse Substrings Between Each Pair of Parentheses
sidebar_label: 1190. Reverse Substrings Between Each Pair of Parentheses
sidebar_position: 1190
---

# [1190. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/)

```py title=reverse-substrings-between-each-pair-of-parentheses.py
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for c in s:
            if c == "(":
                stack.append([])
            elif c == ")":
                words = stack.pop()[::-1]
                if stack:
                    stack[-1] += words
                else:
                    stack.append(words)
            else:
                if stack:
                    stack[-1].append(c)
                else:
                    stack.append([c])
        
        return "".join(stack[-1])
```


