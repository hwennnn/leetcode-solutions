---
id: validate-stack-sequences
title: Validate Stack Sequences
description: Problem Description and Solution for Validate Stack Sequences
sidebar_label: 946. Validate Stack Sequences
sidebar_position: 946
---

# [946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/)

```py title=validate-stack-sequences.py
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        curr = 0
        
        for x in pushed:
            stack.append(x)
            
            while stack and curr < n and stack[-1] == popped[curr]:
                stack.pop()
                curr += 1
            
        return len(stack) == 0 and curr == n
```


