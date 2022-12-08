---
id: intersection-of-two-arrays-ii
title: Intersection of Two Arrays II
description: Problem Description and Solution for Intersection of Two Arrays II
sidebar_label: 350. Intersection of Two Arrays II
sidebar_position: 350
---

# [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)

```py title=intersection-of-two-arrays-ii.py
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < len(nums1): return self.intersect(nums2, nums1)
        
        counter = collections.Counter(nums1)
        res = []
        
        for x in nums2:
            if counter[x] > 0:
                res.append(x)
                counter[x] -= 1
        
        return res
        
```


