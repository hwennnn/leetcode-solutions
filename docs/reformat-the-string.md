---
id: reformat-the-string
title: Reformat The String
description: Problem Description and Solution for Reformat The String
sidebar_label: 1417. Reformat The String
sidebar_position: 1417
---

# [1417. Reformat The String](https://leetcode.com/problems/reformat-the-string/)

```py title=reformat-the-string.py
class Solution:
    def reformat(self, S: str) -> str:
        
        if len(S) == 1: return S
        
        chars, nums = [], []
        
        for s in S:
            if s.isalpha():
                chars.append(s)
            else:
                nums.append(s)
        
        if not chars or not nums: return ""
        
        res = []
        n1, n2 = len(chars), len(nums)
        
        if len(nums) > len(chars): 
            res.append(nums[0])
            for i in range(max(n1,n2)):
                if i < n1:
                    res.append(chars[i])
                    
                if i + 1 < n2:
                    res.append(nums[i+1])
                
        else:
            res.append(chars[0])
            for i in range(max(n1,n2)):
                if i < n2:
                    res.append(nums[i])
                if i + 1 < n1:
                    res.append(chars[i+1])
        
        
        return "".join(res)
```


