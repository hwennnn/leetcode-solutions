---
id: restore-ip-addresses
title: Restore IP Addresses
description: Problem Description and Solution for Restore IP Addresses
sidebar_label: 93. Restore IP Addresses
sidebar_position: 93
---

# [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

```py title=restore-ip-addresses.py
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        
        def backtrack(i, current, count):
            if count > 4: return
            if i == n and count == 4:
                res.append(current)
                return
            
            for j in range(1, 4):
                if i + j > n: break
                word = s[i : i + j]

                if (len(word) > 1 and word[0] == '0') or int(word) > 255: continue
                        
                backtrack(i + j, current + word + ('' if count == 3 else '.'), count + 1)
                
        backtrack(0, '', 0)
        return res
                
            
```


