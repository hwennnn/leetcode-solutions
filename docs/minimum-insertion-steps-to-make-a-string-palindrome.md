---
id: minimum-insertion-steps-to-make-a-string-palindrome
title: Minimum Insertion Steps to Make a String Palindrome
description: Problem Description and Solution for Minimum Insertion Steps to Make a String Palindrome
sidebar_label: 1312. Minimum Insertion Steps to Make a String Palindrome
sidebar_position: 1312
---

# [1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/)

```py title=minimum-insertion-steps-to-make-a-string-palindrome.py
class Solution:
    def lps(self, start, end, s, mem):
        if start == end: return 1
        if start > end: return 0
        if mem[start][end]: return mem[start][end]
        
        mem[start][end] = 2 + self.lps(start+1, end-1, s, mem) if s[start] == s[end] else max(self.lps(start, end-1, s, mem), self.lps(start+1, end, s, mem))
        
        return mem[start][end]
    
    def minInsertions(self, s: str) -> int:
        n = len(s)
        mem = [[0]*n for _ in range(n)]    
        
        return n - self.lps(0, n-1, s, mem)
```


