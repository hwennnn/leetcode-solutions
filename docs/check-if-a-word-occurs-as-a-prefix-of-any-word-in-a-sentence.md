---
id: check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
title: Check If a Word Occurs As a Prefix of Any Word in a Sentence
description: Problem Description and Solution for Check If a Word Occurs As a Prefix of Any Word in a Sentence
sidebar_label: 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
sidebar_position: 1455
---

# [1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

```py title=check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence.py
class Solution:
    def isPrefixOfWord(self, sentence: str, sw: str) -> int:
        S = sentence.split()
        
        l = 0
        for s in S:
            l += 1
            if len(sw) > len(s): continue
            check = True
            for i in range(min(len(s), len(sw))):
                if sw[i] != s[i]:
                    check = False
                    break
            
            if check:
                return l
            
        
        return -1
```


