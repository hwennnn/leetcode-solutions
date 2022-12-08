---
id: max-difference-you-can-get-from-changing-an-integer
title: Max Difference You Can Get From Changing an Integer
description: Problem Description and Solution for Max Difference You Can Get From Changing an Integer
sidebar_label: 1432. Max Difference You Can Get From Changing an Integer
sidebar_position: 1432
---

# [1432. Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/)

```py title=max-difference-you-can-get-from-changing-an-integer.py
class Solution:
    def maxDiff(self, num: int) -> int:
        
        a = b = str(num)
        
        for c in a:
            if c != "9":
                a = a.replace(c,"9")
                break
        
        if b[0] != "1":
            b = b.replace(b[0], "1")
        else:
            for c in b[1:]:
                if c not in "01":
                    b = b.replace(c, "0")
                    break
        
        return int(a) - int(b)
            
```


