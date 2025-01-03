---
title: 67. Add Binary
draft: false
tags: 
  - math
  - string
  - bit-manipulation
  - simulation
date: 2023-02-14
---

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-blue.svg)

## Description

---
<p>Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a binary string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = "11", b = "1"
<strong>Output:</strong> "100"
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = "1010", b = "1011"
<strong>Output:</strong> "10101"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> and <code>b</code> consist&nbsp;only of <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code> characters.</li>
	<li>Each string does not contain leading zeros except for the zero itself.</li>
</ul>


## Solution

---
### Python
``` py title='add-binary'
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n1, n2 = len(a), len(b)
        i, j = n1 - 1, n2 - 1
        res = []
        
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0:
                carry += int(a[i] == "1")
                i -= 1
                
            if j >= 0:
                carry += int(b[j] == "1")
                j -= 1
            
            res.append(str(carry % 2))
            carry //= 2
        
        return "".join(res[::-1])

```

