---
title: 131. Palindrome Partitioning
draft: false
tags: 
  - string
  - dynamic-programming
  - backtracking
date: 2024-05-22
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
<p>Given a string <code>s</code>, partition <code>s</code> such that every <span data-keyword="substring-nonempty">substring</span> of the partition is a <span data-keyword="palindrome-string"><strong>palindrome</strong></span>. Return <em>all possible palindrome partitioning of </em><code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>


## Solution

---
### Python
``` py title='palindrome-partitioning'
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        res = []

        def isPal(x):
            M = len(x)
            i, j = 0, M - 1

            while i <= j and x[i] == x[j]:
                i += 1
                j -= 1
            
            return i >= j

        def backtrack(index, curr):
            nonlocal res

            if index >= N:
                res.append(curr[:])
                return
            
            for j in range(index, N):
                if isPal(s[index: j + 1]):
                    curr.append(s[index : j + 1])
                    backtrack(j + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return res

```

