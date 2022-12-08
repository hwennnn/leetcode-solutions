---
id: count-vowel-substrings-of-a-string
title: Count Vowel Substrings of a String
description: Problem Description and Solution for Count Vowel Substrings of a String
sidebar_label: 2062. Count Vowel Substrings of a String
sidebar_position: 2062
---

# [2062. Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/)

```py title=count-vowel-substrings-of-a-string.py
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        
        n = len(word)
        
        for i in range(n):
            A = [0, 0, 0, 0, 0]
            for j in range(i, n):
                if word[j] == 'a':
                    A[0] += 1
                elif word[j] == 'e':
                    A[1] += 1
                elif word[j] == 'i':
                    A[2] += 1
                elif word[j] == 'o':
                    A[3] += 1
                elif word[j] == 'u':
                    A[4] += 1
                else:
                    break
                
                if all(x > 0 for x in A):
                    res += 1

        return res
```


