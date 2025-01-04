---
title: 516. Longest Palindromic Subsequence
draft: false
tags: 
  - leetcode-medium
  - string
  - dynamic-programming
date: 2020-08-24
---

[Problem Link](https://leetcode.com/problems/longest-palindromic-subsequence/)

## Description

---
<p>Given a string <code>s</code>, find <em>the longest palindromic <strong>subsequence</strong>&#39;s length in</em> <code>s</code>.</p>

<p>A <strong>subsequence</strong> is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;bbbab&quot;
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible longest palindromic subsequence is &quot;bbbb&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> One possible longest palindromic subsequence is &quot;bb&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


## Solution

---
### Python
``` py title='longest-palindromic-subsequence'
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)

        @cache
        def go(i, j):
            if i == j: return 1
            if i > j: return 0

            if s[i] == s[j]:
                return 2 + go(i + 1, j - 1)
            
            return max(go(i + 1, j), go(i, j - 1))
        
        return go(0, N - 1)
```
### C++
``` cpp title='longest-palindromic-subsequence'
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

