---
id: letter-combinations-of-a-phone-number
title: Letter Combinations of a Phone Number
description: Problem Description and Solution for Letter Combinations of a Phone Number
sidebar_label: 17. Letter Combinations of a Phone Number
sidebar_position: 17
---

# [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

```py title=letter-combinations-of-a-phone-number.py
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        mp = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        n = len(digits)
        res = []
        
        def go(index, curr):
            if index == n:
                res.append(curr)
                return
            
            for x in mp[int(digits[index])]:
                go(index + 1, curr + x)
            
        go(0, "")
            
        return res
```


