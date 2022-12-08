---
id: longest-chunked-palindrome-decomposition
title: Longest Chunked Palindrome Decomposition
description: Problem Description and Solution for Longest Chunked Palindrome Decomposition
sidebar_label: 1147. Longest Chunked Palindrome Decomposition
sidebar_position: 1147
---

# [1147. Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)

```py title=longest-chunked-palindrome-decomposition.py
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        
        for i in range(n // 2):
            if text[:i + 1] == text[n - i - 1:]:
                return 2 + self.longestDecomposition(text[i + 1: n - i - 1])
        
        return 0 if n == 0 else 1
```


