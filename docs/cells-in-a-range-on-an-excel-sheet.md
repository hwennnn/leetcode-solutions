---
id: cells-in-a-range-on-an-excel-sheet
title: Cells in a Range on an Excel Sheet
description: Problem Description and Solution for Cells in a Range on an Excel Sheet
sidebar_label: 2194. Cells in a Range on an Excel Sheet
sidebar_position: 2194
---

# [2194. Cells in a Range on an Excel Sheet](https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/)

```py title=cells-in-a-range-on-an-excel-sheet.py
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = s
        res = []
        
        for c in range(ord(c1), ord(c2) + 1):
            for r in range(ord(r1), ord(r2) + 1):
                res.append(chr(c) + chr(r))
        
        return res
```


