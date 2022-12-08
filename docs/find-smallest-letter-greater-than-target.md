---
id: find-smallest-letter-greater-than-target
title: Find Smallest Letter Greater Than Target
description: Problem Description and Solution for Find Smallest Letter Greater Than Target
sidebar_label: 744. Find Smallest Letter Greater Than Target
sidebar_position: 744
---

# [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)

```py title=find-smallest-letter-greater-than-target.py
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        count = [0] * 26
        
        for x in letters:
            index = ord(x) - ord("a")
            count[index] += 1
        
        index = ord(target) - ord("a") + 1
        
        for i in range(26):
            if count[(index + i) % 26] > 0:
                return chr(ord("a") + (index + i) % 26)
        
        
```


