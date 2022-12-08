---
id: kth-distinct-string-in-an-array
title: Kth Distinct String in an Array
description: Problem Description and Solution for Kth Distinct String in an Array
sidebar_label: 2053. Kth Distinct String in an Array
sidebar_position: 2053
---

# [2053. Kth Distinct String in an Array](https://leetcode.com/problems/kth-distinct-string-in-an-array/)

```py title=kth-distinct-string-in-an-array.py
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = collections.Counter(arr)
        
        for x, v in counter.items():
            if v == 1:
                k -= 1
                
                if k == 0: return x
        
        return ""
```


