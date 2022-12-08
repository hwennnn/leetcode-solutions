---
id: length-of-last-word
title: Length of Last Word
description: Problem Description and Solution for Length of Last Word
sidebar_label: 58. Length of Last Word
sidebar_position: 58
---

# [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

```py title=length-of-last-word.py
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        
        return len(s[-1])
```


