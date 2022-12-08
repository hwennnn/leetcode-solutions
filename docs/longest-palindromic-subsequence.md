---
id: longest-palindromic-subsequence
title: Longest Palindromic Subsequence
description: Problem Description and Solution for Longest Palindromic Subsequence
sidebar_label: 516. Longest Palindromic Subsequence
sidebar_position: 516
---

# [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)

```py title=longest-palindromic-subsequence.py
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def go(i, j):
            if i == j: return 1
            if i > j: return 0
            
            return 2 + go(i + 1, j - 1) if s[i] == s[j] else max(go(i + 1, j), go(i, j - 1))
        
        return go(0, len(s) - 1)
```

```cpp title=longest-palindromic-subsequence.cpp
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        vector<vector<int>> mem(n,vector<int>(n));
        
        return helper(0, n-1, s, mem);
    }
    
    int helper(int start, int end, string &s, vector<vector<int>> &mem){
        if (start == end) return 1;
        if (start > end) return 0 ;
        if (mem[start][end]) return mem[start][end];
        
        return mem[start][end] = s[start] == s[end] ? 2 + helper(start+1, end-1, s, mem) : 
        max(helper(start+1,end,s, mem), helper(start, end -1,s, mem));
    }
};
```


