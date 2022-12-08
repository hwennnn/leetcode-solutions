---
id: remove-all-adjacent-duplicates-in-string
title: Remove All Adjacent Duplicates In String
description: Problem Description and Solution for Remove All Adjacent Duplicates In String
sidebar_label: 1047. Remove All Adjacent Duplicates In String
sidebar_position: 1047
---

# [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)

```py title=remove-all-adjacent-duplicates-in-string.py
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for x in s:
            stack.append(x)
            
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        
        return "".join(stack)



```


