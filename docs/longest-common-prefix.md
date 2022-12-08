---
id: longest-common-prefix
title: Longest Common Prefix
description: Problem Description and Solution for Longest Common Prefix
sidebar_label: 14. Longest Common Prefix
sidebar_position: 14
---

# [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

```py title=longest-common-prefix.py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        w = min(strs, key = len)
        res = ""
        
        for i, x in enumerate(w):
            flag = True
            
            for word in strs:
                if word[i] != x:
                    flag = False
                    break
            
            if flag:
                res += x
            else:
                break
        
        return res
```


