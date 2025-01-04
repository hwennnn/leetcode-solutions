---
title: 69. Sqrt(x)
draft: false
tags: 
  - leetcode-easy
  - math
  - binary-search
date: 2022-05-14
---

[Problem Link](https://leetcode.com/problems/sqrtx/)

## Description

---
<p>Given a non-negative integer <code>x</code>, return <em>the square root of </em><code>x</code><em> rounded down to the nearest integer</em>. The returned integer should be <strong>non-negative</strong> as well.</p>

<p>You <strong>must not use</strong> any built-in exponent function or operator.</p>

<ul>
	<li>For example, do not use <code>pow(x, 0.5)</code> in c++ or <code>x ** 0.5</code> in python.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 4 is 2, so we return 2.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 8
<strong>Output:</strong> 2
<strong>Explanation:</strong> The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## Solution

---
### Python
``` py title='sqrtx'
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        
        def good(v):
            return v*v <= x
        
        left, right = 0, x
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                left = mid + 1
            else:
                right = mid
        
        return left - 1
```

