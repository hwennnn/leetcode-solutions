---
id: intersection-of-two-arrays
title: Intersection of Two Arrays
description: Problem Description and Solution for Intersection of Two Arrays
sidebar_label: 349. Intersection of Two Arrays
sidebar_position: 349
---

# [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

```py title=intersection-of-two-arrays.py
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        temp1 = collections.Counter(nums1)
        
        temp2 = collections.Counter(nums2)
        
        temp = []
        
        for i in temp1:
            
            if i in temp2:
                if max(temp1[i],temp2[i],0)>0:
                    temp.append(i)
                    
        return temp
```


