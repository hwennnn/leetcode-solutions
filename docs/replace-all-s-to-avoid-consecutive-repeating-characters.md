---
id: replace-all-s-to-avoid-consecutive-repeating-characters
title: Replace All ?'s to Avoid Consecutive Repeating Characters
description: Problem Description and Solution for Replace All ?'s to Avoid Consecutive Repeating Characters
sidebar_label: 1576. Replace All ?'s to Avoid Consecutive Repeating Characters
sidebar_position: 1576
---

# [1576. Replace All ?'s to Avoid Consecutive Repeating Characters](https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/)

```py title=replace-all-s-to-avoid-consecutive-repeating-characters.py
class Solution:
    def modifyString(self, s: str) -> str:
        n = len(s)
        
        string = "abcdefghijklmnopqrstuvwxyz"
        res = ""
        
        for i in range(n):
            
            if s[i] == "?":
                left_idx = ord(res[i-1]) - 97 if i > 0 else -1
                right_idx = ord(s[i+1]) - 97 if i+1 <= n-1 else -1
                idx = (left_idx + 2)%26 if left_idx != -1 else (right_idx + 1)%26
                
                while (idx == left_idx or idx == right_idx):
                    idx = (idx + 1)%26
                res += string[idx]

            else:
                res += s[i]
        return res
```


