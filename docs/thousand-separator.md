---
id: thousand-separator
title: Thousand Separator
description: Problem Description and Solution for Thousand Separator
sidebar_label: 1556. Thousand Separator
sidebar_position: 1556
---

# [1556. Thousand Separator](https://leetcode.com/problems/thousand-separator/)

```py title=thousand-separator.py
class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        ans = ""
        i = 0
        
        for s in reversed(str(n)):
            if i !=0 and i%3==0:
                ans += "."
            ans += s
            i+=1
        
        ans = ans[::-1]
        
        return ans
```


