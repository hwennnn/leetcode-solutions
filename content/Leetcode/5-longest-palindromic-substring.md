---
title: 5. Longest Palindromic Substring
draft: false
tags: 
  - leetcode-medium
  - two-pointers
  - string
  - dynamic-programming
date: 2024-08-14
---

[Problem Link](https://leetcode.com/problems/longest-palindromic-substring/)

## Description

---
<p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string"><em>palindromic</em></span> <span data-keyword="substring-nonempty"><em>substring</em></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Explanation:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>


## Solution

---
### Python
``` py title='longest-palindromic-substring'
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)

        if N == 1: return s

        def pal(i, j):
            while i >= 0 and j < N and s[i] == s[j]:
                i -= 1
                j += 1
            
            i += 1
            j -= 1
            
            return s[i : j + 1]
        
        res = ""
        for i in range(N - 1):
            res = max(res, pal(i, i), pal(i, i + 1), key = len)
        
        return res

```

