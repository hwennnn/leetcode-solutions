---
id: check-if-all-the-integers-in-a-range-are-covered
title: Check if All the Integers in a Range Are Covered
description: Problem Description and Solution for Check if All the Integers in a Range Are Covered
sidebar_label: 1893. Check if All the Integers in a Range Are Covered
sidebar_position: 1893
---

# [1893. Check if All the Integers in a Range Are Covered](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/)

```py title=check-if-all-the-integers-in-a-range-are-covered.py
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for x in range(left, right + 1):
            ok = 0
            for start, end in ranges:
                if start <= x <= end:
                    ok = 1
                    break
            
            if not ok: return False
        
        return True
```


