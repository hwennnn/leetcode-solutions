---
title: 371. Sum of Two Integers
draft: false
tags: 
  - leetcode-medium
  - math
  - bit-manipulation
date: 2025-01-23
---

[Problem Link](https://leetcode.com/problems/sum-of-two-integers/)

## Description

---
<p>Given two integers <code>a</code> and <code>b</code>, return <em>the sum of the two integers without using the operators</em> <code>+</code> <em>and</em> <code>-</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> a = 1, b = 2
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> a = 2, b = 3
<strong>Output:</strong> 5
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-1000 &lt;= a, b &lt;= 1000</code></li>
</ul>


## Solution

---
### Python3
``` py title='sum-of-two-integers'
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff
        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        # for overflow condition like
        # -1
        #  1
        return a&mask if b > mask else a
```

