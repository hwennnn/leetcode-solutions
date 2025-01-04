---
title: 214. Shortest Palindrome
draft: false
tags: 
  - leetcode-hard
  - string
  - rolling-hash
  - string-matching
  - hash-function
date: 2024-09-20
---

[Problem Link](https://leetcode.com/problems/shortest-palindrome/)

## Description

---
<p>You are given a string <code>s</code>. You can convert <code>s</code> to a <span data-keyword="palindrome-string">palindrome</span> by adding characters in front of it.</p>

<p>Return <em>the shortest palindrome you can find by performing this transformation</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aacecaaa"
<strong>Output:</strong> "aaacecaaa"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "abcd"
<strong>Output:</strong> "dcbabcd"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters only.</li>
</ul>


## Solution

---
### Python3
``` py title='shortest-palindrome'
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
```

