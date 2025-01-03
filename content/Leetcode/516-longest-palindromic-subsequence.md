---
title: 516. Longest Palindromic Subsequence
draft: false
tags: 
  - string
  - dynamic-programming
date: 2024-08-14
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

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

