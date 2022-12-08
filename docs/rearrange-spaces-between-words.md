---
id: rearrange-spaces-between-words
title: Rearrange Spaces Between Words
description: Problem Description and Solution for Rearrange Spaces Between Words
sidebar_label: 1592. Rearrange Spaces Between Words
sidebar_position: 1592
---

# [1592. Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/)

```py title=rearrange-spaces-between-words.py
class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        texts = text.split()
        spaces = 0
        
        for i in text:
            if i == " ":
                spaces += 1
        if len(texts) == 1:
            return texts[0] + " " * spaces
            
        between = spaces // (len(texts)-1)
        leftover = spaces % (len(texts)-1)
        
        return (" " * between).join(texts) + " "*leftover
```


