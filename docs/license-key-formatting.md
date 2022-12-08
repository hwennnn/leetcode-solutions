---
id: license-key-formatting
title: License Key Formatting
description: Problem Description and Solution for License Key Formatting
sidebar_label: 482. License Key Formatting
sidebar_position: 482
---

# [482. License Key Formatting](https://leetcode.com/problems/license-key-formatting/)

```py title=license-key-formatting.py
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.split('-')
        words = "".join(s)
        n = len(words)
        
        M = n % k
        start = M if M != 0 else k
        res = []
        res.append(words[:start].upper())

        for i in range(start, n, k):
            res.append(words[i : min(n, i + k)].upper())
        
        return "-".join(res)
        
        
                
            
```


