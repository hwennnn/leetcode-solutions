---
id: decompress-run-length-encoded-list
title: Decompress Run-Length Encoded List
description: Problem Description and Solution for Decompress Run-Length Encoded List
sidebar_label: 1313. Decompress Run-Length Encoded List
sidebar_position: 1313
---

# [1313. Decompress Run-Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/)

```py title=decompress-run-length-encoded-list.py
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(0,n,2):
            for _ in range(nums[i]):
                res.append(nums[i+1])
        
        return res
```


