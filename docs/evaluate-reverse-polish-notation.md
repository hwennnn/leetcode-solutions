---
id: evaluate-reverse-polish-notation
title: Evaluate Reverse Polish Notation
description: Problem Description and Solution for Evaluate Reverse Polish Notation
sidebar_label: 150. Evaluate Reverse Polish Notation
sidebar_position: 150
---

# [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

```py title=evaluate-reverse-polish-notation.py
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first / second))
            else:
                stack.append(int(c))

        return stack.pop()
```


