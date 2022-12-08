---
id: distant-barcodes
title: Distant Barcodes
description: Problem Description and Solution for Distant Barcodes
sidebar_label: 1054. Distant Barcodes
sidebar_position: 1054
---

# [1054. Distant Barcodes](https://leetcode.com/problems/distant-barcodes/)

```py title=distant-barcodes.py
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = collections.Counter(barcodes)
        count = sorted([(counter[x], x) for x in counter], key = lambda x : -x[0])
        i = 0
        n = len(barcodes)
        res = [None] * n
        
        for cnt,key in count:
            for _ in range(cnt):
                if i >= n: i = 1
                res[i] = key
                i += 2
        
        return res
        
```


