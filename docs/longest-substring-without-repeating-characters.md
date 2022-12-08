---
id: longest-substring-without-repeating-characters
title: Longest Substring Without Repeating Characters
description: Problem Description and Solution for Longest Substring Without Repeating Characters
sidebar_label: 3. Longest Substring Without Repeating Characters
sidebar_position: 3
---

# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```py title=longest-substring-without-repeating-characters.py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i = 0
        res = 0
        
        for j, x in enumerate(s):
            while x in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(x)
            
            res = max(res, j - i + 1)
            
        return res
            
```


