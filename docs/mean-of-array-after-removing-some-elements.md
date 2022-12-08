---
id: mean-of-array-after-removing-some-elements
title: Mean of Array After Removing Some Elements
description: Problem Description and Solution for Mean of Array After Removing Some Elements
sidebar_label: 1619. Mean of Array After Removing Some Elements
sidebar_position: 1619
---

# [1619. Mean of Array After Removing Some Elements](https://leetcode.com/problems/mean-of-array-after-removing-some-elements/)

```py title=mean-of-array-after-removing-some-elements.py
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        k = int(len(arr)*0.05)
        
        arr.sort()
        count = res = 0
        
        for i in range(k,n-k):
            res += 1
            count += arr[i]
        
        return count / res
            
```


