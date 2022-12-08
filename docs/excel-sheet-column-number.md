---
id: excel-sheet-column-number
title: Excel Sheet Column Number
description: Problem Description and Solution for Excel Sheet Column Number
sidebar_label: 171. Excel Sheet Column Number
sidebar_position: 171
---

# [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

```py title=excel-sheet-column-number.py
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        
        for x in columnTitle:
            res = res * 26 + ord(x) - ord('A') + 1
        
        return res
```


