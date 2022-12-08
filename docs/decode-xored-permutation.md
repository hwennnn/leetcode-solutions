---
id: decode-xored-permutation
title: Decode XORed Permutation
description: Problem Description and Solution for Decode XORed Permutation
sidebar_label: 1734. Decode XORed Permutation
sidebar_position: 1734
---

# [1734. Decode XORed Permutation](https://leetcode.com/problems/decode-xored-permutation/)

```py title=decode-xored-permutation.py
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        curr = start = 0
        
        for i in range(1, len(encoded)+2):
            start ^= i
        
        for x in encoded:
            curr ^= x
            start ^= curr
        
        res = [start]
        for x in encoded:
            res.append(res[-1] ^ x)
        
        return res
```


