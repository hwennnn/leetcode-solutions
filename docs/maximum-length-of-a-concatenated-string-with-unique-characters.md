---
id: maximum-length-of-a-concatenated-string-with-unique-characters
title: Maximum Length of a Concatenated String with Unique Characters
description: Problem Description and Solution for Maximum Length of a Concatenated String with Unique Characters
sidebar_label: 1239. Maximum Length of a Concatenated String with Unique Characters
sidebar_position: 1239
---

# [1239. Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

```py title=maximum-length-of-a-concatenated-string-with-unique-characters.py
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        N = len(arr)
        
        @cache
        def go(index, mask):
            if index == N: return 0
            
            res = go(index + 1, mask)
            valid = True
            curr = mask
            
            for char in arr[index]:
                k = ord(char) - ord("a")
                if curr & (1 << k) > 0:
                    valid = False
                    break
                else:
                    curr ^= (1 << k)
            
            if valid:  
                res = max(res, len(arr[index]) + go(index + 1, curr))
            
            return res
                
        return go(0, 0)
```


