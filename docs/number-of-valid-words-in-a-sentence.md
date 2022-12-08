---
id: number-of-valid-words-in-a-sentence
title: Number of Valid Words in a Sentence
description: Problem Description and Solution for Number of Valid Words in a Sentence
sidebar_label: 2047. Number of Valid Words in a Sentence
sidebar_position: 2047
---

# [2047. Number of Valid Words in a Sentence](https://leetcode.com/problems/number-of-valid-words-in-a-sentence/)

```py title=number-of-valid-words-in-a-sentence.py
class Solution:
    def countValidWords(self, sentence: str) -> int:
        res = 0
        
        for s in sentence.split():
            if any(c in s for c in "0123456789"):
                continue
            
            if s.count('-') > 1 or s[0] == '-' or s[-1] == '-':
                continue
            
            if '-' in s:
                index = s.index('-')
                if not s[index - 1].isalpha() or not s[index + 1].isalpha():
                    continue
            
            if sum(c in '!.,' for c in s) > 1:
                continue
            
            if any(c in '!.,' for c in s[:-1]):
                continue
            res += 1
            
        return res
```


