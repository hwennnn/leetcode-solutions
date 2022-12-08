---
id: remove-duplicate-letters
title: Remove Duplicate Letters
description: Problem Description and Solution for Remove Duplicate Letters
sidebar_label: 316. Remove Duplicate Letters
sidebar_position: 316
---

# [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters/)

```py title=remove-duplicate-letters.py
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        put = set()
        
        for x in s:
            counter[x] -= 1
            
            if x in put: continue
                
            while stack and x < stack[-1] and counter[stack[-1]] > 0:
                put.remove(stack.pop())
            
            stack.append(x)
            put.add(x)

        return "".join(stack)
```


