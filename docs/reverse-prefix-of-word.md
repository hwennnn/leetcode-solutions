---
id: reverse-prefix-of-word
title: Reverse Prefix of Word
description: Problem Description and Solution for Reverse Prefix of Word
sidebar_label: 2000. Reverse Prefix of Word
sidebar_position: 2000
---

# [2000. Reverse Prefix of Word](https://leetcode.com/problems/reverse-prefix-of-word/)

```py title=reverse-prefix-of-word.py
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        
        for i,x in enumerate(word):
            if ch == x:
                index = i
                break
        
        if index == -1: return word
        return word[:index + 1][::-1] + word[index + 1:]
```


