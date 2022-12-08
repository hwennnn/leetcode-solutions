---
id: maximum-number-of-words-you-can-type
title: Maximum Number of Words You Can Type
description: Problem Description and Solution for Maximum Number of Words You Can Type
sidebar_label: 1935. Maximum Number of Words You Can Type
sidebar_position: 1935
---

# [1935. Maximum Number of Words You Can Type](https://leetcode.com/problems/maximum-number-of-words-you-can-type/)

```py title=maximum-number-of-words-you-can-type.py
class Solution:
    def canBeTypedWords(self, text: str, letters: str) -> int:
        text = text.split(' ')
        ss = set(letters)
        res = len(text)
        
        for t in text:
            if set(t) & ss:
                res -= 1
        
        return res
```


