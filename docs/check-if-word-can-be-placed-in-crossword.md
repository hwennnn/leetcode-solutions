---
id: check-if-word-can-be-placed-in-crossword
title: Check if Word Can Be Placed In Crossword
description: Problem Description and Solution for Check if Word Can Be Placed In Crossword
sidebar_label: 2018. Check if Word Can Be Placed In Crossword
sidebar_position: 2018
---

# [2018. Check if Word Can Be Placed In Crossword](https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/)

```py title=check-if-word-can-be-placed-in-crossword.py
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words = [word, word[::-1]]
        n = len(word)
        
        for B in board, zip(*board):
            for row in B:
                s = "".join(row).split('#')
                
                for word in words:
                    for z in s:
                        if len(z) == n and all(z[i] == word[i] or z[i] == ' ' for i in range(n)):
                            return True
        
        return False
```


