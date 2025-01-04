---
title: 1405. Longest Happy String
draft: false
tags: 
  - leetcode-medium
  - string
  - greedy
  - heap-priority-queue
date: 2024-10-16
---

[Problem Link](https://leetcode.com/problems/longest-happy-string/)

## Description

---
<p>A string <code>s</code> is called <strong>happy</strong> if it satisfies the following conditions:</p>

<ul>
	<li><code>s</code> only contains the letters <code>&#39;a&#39;</code>, <code>&#39;b&#39;</code>, and <code>&#39;c&#39;</code>.</li>
	<li><code>s</code> does not contain any of <code>&quot;aaa&quot;</code>, <code>&quot;bbb&quot;</code>, or <code>&quot;ccc&quot;</code> as a substring.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>a</code> occurrences of the letter <code>&#39;a&#39;</code>.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>b</code> occurrences of the letter <code>&#39;b&#39;</code>.</li>
	<li><code>s</code> contains <strong>at most</strong> <code>c</code> occurrences of the letter <code>&#39;c&#39;</code>.</li>
</ul>

<p>Given three integers <code>a</code>, <code>b</code>, and <code>c</code>, return <em>the <strong>longest possible happy </strong>string</em>. If there are multiple longest happy strings, return <em>any of them</em>. If there is no such string, return <em>the empty string </em><code>&quot;&quot;</code>.</p>

<p>A <strong>substring</strong> is a contiguous sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> a = 1, b = 1, c = 7
<strong>Output:</strong> &quot;ccaccbcc&quot;
<strong>Explanation:</strong> &quot;ccbccacc&quot; would also be a correct answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> a = 7, b = 1, c = 0
<strong>Output:</strong> &quot;aabaa&quot;
<strong>Explanation:</strong> It is the only correct answer in this case.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= a, b, c &lt;= 100</code></li>
	<li><code>a + b + c &gt; 0</code></li>
</ul>


## Solution

---
### Python
``` py title='longest-happy-string'
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        size = a + b + c
        A, B, C = 0, 0, 0
        res = ""
        
        for i in range(size):
            if (a >= b and a >= c and A != 2) or (B == 2 and a > 0) or (C == 2 and a > 0):
                res += "a"
                a -= 1
                A += 1
                B = 0
                C = 0
            
            elif (b >= a and b >= c and B != 2) or (A == 2 and b > 0) or (C == 2 and b > 0):
                res += "b"
                b -= 1
                B += 1
                A = 0
                C = 0
            
            elif (c >= a and c >= b and C != 2) or (A == 2 and c > 0) or (B == 2 and c > 0):
                res += "c"
                c -= 1
                C += 1
                A = 0
                B = 0
        
        return res
```

