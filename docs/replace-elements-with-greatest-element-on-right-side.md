---
id: replace-elements-with-greatest-element-on-right-side
title: Replace Elements with Greatest Element on Right Side
description: Problem Description and Solution for Replace Elements with Greatest Element on Right Side
sidebar_label: 1299. Replace Elements with Greatest Element on Right Side
sidebar_position: 1299
---

# [1299. Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)

```py title=replace-elements-with-greatest-element-on-right-side.py
class Solution:
    def replaceElements(self, A: List[int]) -> List[int]:
        mx = -1
        
        for i in range(len(A)-1, -1, -1):
            A[i],mx = mx, max(A[i], mx)
        
        return A
```


