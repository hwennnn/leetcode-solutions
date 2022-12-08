---
id: defuse-the-bomb
title: Defuse the Bomb
description: Problem Description and Solution for Defuse the Bomb
sidebar_label: 1652. Defuse the Bomb
sidebar_position: 1652
---

# [1652. Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/)

```py title=defuse-the-bomb.py
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0: return [0] * n
        res = []
        
        for i,x in enumerate(code):
            num = 0
            for _ in range(abs(k)):
                if k < 0:
                    i = (i-1)%n
                else:
                    i = (i+1)%n
                num += code[i]
            
            res.append(num)
        
        return res
```


