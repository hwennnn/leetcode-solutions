---
id: decode-xored-array
title: Decode XORed Array
description: Problem Description and Solution for Decode XORed Array
sidebar_label: 1720. Decode XORed Array
sidebar_position: 1720
---

# [1720. Decode XORed Array](https://leetcode.com/problems/decode-xored-array/)

```py title=decode-xored-array.py
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        
        for i in range(len(encoded)):
            res.append(res[-1] ^ encoded[i])
        
        return res
```


