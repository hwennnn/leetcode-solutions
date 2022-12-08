---
id: two-out-of-three
title: Two Out of Three
description: Problem Description and Solution for Two Out of Three
sidebar_label: 2032. Two Out of Three
sidebar_position: 2032
---

# [2032. Two Out of Three](https://leetcode.com/problems/two-out-of-three/)

```py title=two-out-of-three.py
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        res = []
        mp = collections.defaultdict(int)
        
        for x in nums1:
            mp[x] += 1
        for x in nums2:
            mp[x] += 1
        for x in nums3:
            mp[x] += 1
            
        for k,v in mp.items():
            if v >= 2:
                res.append(k)
        
        return res
```


