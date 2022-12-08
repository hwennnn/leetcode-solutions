---
id: check-if-a-string-contains-all-binary-codes-of-size-k
title: Check If a String Contains All Binary Codes of Size K
description: Problem Description and Solution for Check If a String Contains All Binary Codes of Size K
sidebar_label: 1461. Check If a String Contains All Binary Codes of Size K
sidebar_position: 1461
---

# [1461. Check If a String Contains All Binary Codes of Size K](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)

```py title=check-if-a-string-contains-all-binary-codes-of-size-k.py
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        seen = [False] * (1 << k)
        mask = 0
        
        for i, x in enumerate(s):
            if i < k:
                if x == "1":
                    mask |= (1 << i)
            else:
                mask >>= 1
                if x == "1":
                    mask |= (1 << (k - 1))
            
            if i >= k - 1:
                seen[mask] = True
        
        return all(seen[mask] for mask in range(1 << k))
                
```


