---
id: rearrange-words-in-a-sentence
title: Rearrange Words in a Sentence
description: Problem Description and Solution for Rearrange Words in a Sentence
sidebar_label: 1451. Rearrange Words in a Sentence
sidebar_position: 1451
---

# [1451. Rearrange Words in a Sentence](https://leetcode.com/problems/rearrange-words-in-a-sentence/)

```py title=rearrange-words-in-a-sentence.py
class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split()
        text.sort(key = len)
        
        for i in range(len(text)):
            if i == 0:
                text[i] = text[i].capitalize()
            else:
                text[i] = text[i].lower()
                
        return " ".join(text)
```


