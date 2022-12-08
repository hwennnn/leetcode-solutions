---
id: rearrange-characters-to-make-target-string
title: Rearrange Characters to Make Target String
description: Problem Description and Solution for Rearrange Characters to Make Target String
sidebar_label: 2287. Rearrange Characters to Make Target String
sidebar_position: 2287
---

# [2287. Rearrange Characters to Make Target String](https://leetcode.com/problems/rearrange-characters-to-make-target-string/)

```py title=rearrange-characters-to-make-target-string.py
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        tc = Counter(target)
        sc = Counter(s)
        
        return min(sc[t] // tc[t] for t in tc)
```


