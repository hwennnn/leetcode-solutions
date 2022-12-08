---
id: count-elements-with-strictly-smaller-and-greater-elements
title: Count Elements With Strictly Smaller and Greater Elements 
description: Problem Description and Solution for Count Elements With Strictly Smaller and Greater Elements 
sidebar_label: 2148. Count Elements With Strictly Smaller and Greater Elements 
sidebar_position: 2148
---

# [2148. Count Elements With Strictly Smaller and Greater Elements ](https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/)

```py title=count-elements-with-strictly-smaller-and-greater-elements.py
class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        n = len(nums)
        
        for i in range(1, n - 1):
            smaller = False
            
            for j in range(i):
                if nums[j] < nums[i]:
                    smaller = True
                    break
                    
            if not smaller: continue
                
            larger = False
            
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    larger = True
                    break
            
            if not larger: continue
            
            res += 1
        
        
        return res
```


