---
id: smallest-subsequence-of-distinct-characters
title: Smallest Subsequence of Distinct Characters
description: Problem Description and Solution for Smallest Subsequence of Distinct Characters
sidebar_label: 1081. Smallest Subsequence of Distinct Characters
sidebar_position: 1081
---

# [1081. Smallest Subsequence of Distinct Characters](https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/)

```py title=smallest-subsequence-of-distinct-characters.py
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        put = set()
        counter = Counter(s)
        
        for x in s:
            counter[x] -= 1
            
            if x in put: continue
                
            while stack and x < stack[-1] and counter[stack[-1]] > 0:
                put.remove(stack.pop())
            
            stack.append(x)
            put.add(x)
        
        return "".join(stack)
```


