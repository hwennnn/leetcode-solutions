---
id: element-appearing-more-than-25-in-sorted-array
title: Element Appearing More Than 25% In Sorted Array
description: Problem Description and Solution for Element Appearing More Than 25% In Sorted Array
sidebar_label: 1287. Element Appearing More Than 25% In Sorted Array
sidebar_position: 1287
---

# [1287. Element Appearing More Than 25% In Sorted Array](https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/)

```py title=element-appearing-more-than-25-in-sorted-array.py
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        m = len(arr) // 4
        
        for i in range(n-m+1):
            if arr[i] == arr[i+m]:
                return arr[i]
```


