---
title: 132. Palindrome Partitioning II
draft: false
tags: 
  - string
  - dynamic-programming
date: 2021-08-07
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>Given a string <code>s</code>, partition <code>s</code> such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string">palindrome</span>.</p>

<p>Return <em>the <strong>minimum</strong> cuts needed for a palindrome partitioning of</em> <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aab&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong> The palindrome partitioning [&quot;aa&quot;,&quot;b&quot;] could be produced using 1 cut.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ab&quot;
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2000</code></li>
	<li><code>s</code> consists of lowercase English letters only.</li>
</ul>


## Solution

---
### Python
``` py title='palindrome-partitioning-ii'
class Solution:
    def minCut(self, s: str) -> int:
        if len(s) == 1: return 0
        
        n = len(s)
        dp = list(range(n))
        
        for mid in range(1, n):
            
            start = end = mid
            while start >= 0 and end < n and s[start] == s[end]:
                cut = 0 if start == 0 else dp[start - 1] + 1
                dp[end] = min(dp[end], cut)
                start -= 1
                end += 1
            
            start, end = mid - 1, mid
            while start >= 0 and end < n and s[start] == s[end]:
                cut = 0 if start == 0 else dp[start - 1] + 1
                dp[end] = min(dp[end], cut)
                start -= 1
                end += 1
        
        return dp[-1]

```

