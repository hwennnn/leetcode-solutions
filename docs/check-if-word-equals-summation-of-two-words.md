---
id: check-if-word-equals-summation-of-two-words
title: Check if Word Equals Summation of Two Words
description: Problem Description and Solution for Check if Word Equals Summation of Two Words
sidebar_label: 1880. Check if Word Equals Summation of Two Words
sidebar_position: 1880
---

# [1880. Check if Word Equals Summation of Two Words](https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/)

```py title=check-if-word-equals-summation-of-two-words.py
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def helper(word):
            return int("".join(str(ord(c) - ord('a')) for c in word))
        
        return helper(firstWord) + helper(secondWord) == helper(targetWord)
```


