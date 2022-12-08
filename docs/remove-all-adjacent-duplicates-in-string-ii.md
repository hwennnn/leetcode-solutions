---
id: remove-all-adjacent-duplicates-in-string-ii
title: Remove All Adjacent Duplicates in String II
description: Problem Description and Solution for Remove All Adjacent Duplicates in String II
sidebar_label: 1209. Remove All Adjacent Duplicates in String II
sidebar_position: 1209
---

# [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

```py title=remove-all-adjacent-duplicates-in-string-ii.py
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for x in s:
            if stack and stack[-1][0] == x:
                _, cnt = stack.pop()
                stack.append((x, cnt + 1))
            else:
                stack.append((x, 1))
            
            if stack and stack[-1][1] == k:
                stack.pop()
            
        return "".join(x * cnt for x, cnt in stack)
```


