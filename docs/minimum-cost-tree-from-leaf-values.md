---
id: minimum-cost-tree-from-leaf-values
title: Minimum Cost Tree From Leaf Values
description: Problem Description and Solution for Minimum Cost Tree From Leaf Values
sidebar_label: 1130. Minimum Cost Tree From Leaf Values
sidebar_position: 1130
---

# [1130. Minimum Cost Tree From Leaf Values](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/)

```py title=minimum-cost-tree-from-leaf-values.py
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        
        while len(arr) > 1:
            index = arr.index(min(arr))
            
            if 0 < index < len(arr) - 1:
                res += arr[index] * min(arr[index + 1], arr[index - 1])
            else:
                res += arr[index] * (arr[index + 1] if index == 0 else arr[index - 1])
            
            arr.pop(index)
        
        return res
```


