---
id: alphabet-board-path
title: Alphabet Board Path
description: Problem Description and Solution for Alphabet Board Path
sidebar_label: 1138. Alphabet Board Path
sidebar_position: 1138
---

# [1138. Alphabet Board Path](https://leetcode.com/problems/alphabet-board-path/)

```py title=alphabet-board-path.py
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res, i, j = "", 0, 0
        
        for t in target:
            v = ord(t) - ord('a')
            ti, tj = v // 5, v % 5
            
            if ti == i and tj == j:
                res += "!"
            else:
                if ti != i:
                    if ti >= i:
                        if ti == 5 and j != 0:
                            res += "D" * (ti - i - 1)
                        else:
                            res += "D" * (ti - i)
                    else:
                        res += "U" * (i - ti)

                if tj != j:
                    if tj >= j:
                        res += "R" * (tj - j)
                    else:
                        res += "L" * (j - tj)
                    
                    if ti == 5:
                        res += "D"
                    
                res += "!"
                
            i, j = ti, tj
        
        return res
        
```


