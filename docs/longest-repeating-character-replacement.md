---
id: longest-repeating-character-replacement
title: Longest Repeating Character Replacement
description: Problem Description and Solution for Longest Repeating Character Replacement
sidebar_label: 424. Longest Repeating Character Replacement
sidebar_position: 424
---

# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

```py title=longest-repeating-character-replacement.py
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        i = maxCount = res = 0
        
        for j, x in enumerate(s):
            counter[x] += 1
            maxCount = max(maxCount, counter[x])
            
            while j - i + 1 - maxCount > k:
                counter[s[i]] -= 1
                i += 1
            
            res = max(res, j - i + 1)
        
        return res
```


