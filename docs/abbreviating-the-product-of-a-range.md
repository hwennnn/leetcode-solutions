---
id: abbreviating-the-product-of-a-range
title: Abbreviating the Product of a Range
description: Problem Description and Solution for Abbreviating the Product of a Range
sidebar_label: 2117. Abbreviating the Product of a Range
sidebar_position: 2117
---

# [2117. Abbreviating the Product of a Range](https://leetcode.com/problems/abbreviating-the-product-of-a-range/)

```py title=abbreviating-the-product-of-a-range.py
class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        prefixM, suffixM = 10 ** 12, 10 ** 10
        prefix = suffix = 1
        needSplit = False
        trailing = 0
        
        for x in range(left, right + 1):
            prefix *= x
            
            while prefix > prefixM:
                prefix //= 10
            
            suffix *= x
            
            while suffix % 10 == 0:
                suffix //= 10
                trailing += 1
            
            if suffix >= suffixM:
                suffix %= suffixM
                needSplit = True
        
        if not needSplit:
            return f"{suffix}e{trailing}"
        
        return f"{str(prefix)[:5]}...{str(suffix)[-5:]}e{trailing}"
```


