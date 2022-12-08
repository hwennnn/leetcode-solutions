---
id: check-if-string-is-a-prefix-of-array
title: Check If String Is a Prefix of Array
description: Problem Description and Solution for Check If String Is a Prefix of Array
sidebar_label: 1961. Check If String Is a Prefix of Array
sidebar_position: 1961
---

# [1961. Check If String Is a Prefix of Array](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/)

```py title=check-if-string-is-a-prefix-of-array.py
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""
        
        for word in words:
            res += word
            
            if res == s: return True
        
        return False
```


