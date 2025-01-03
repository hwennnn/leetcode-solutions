---
title: 233. Number of Digit One
draft: false
tags: 
  - math
  - dynamic-programming
  - recursion
date: 2023-07-31
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>Given an integer <code>n</code>, count <em>the total number of digit </em><code>1</code><em> appearing in all non-negative integers less than or equal to</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 13
<strong>Output:</strong> 6
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='number-of-digit-one'
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        N = len(s)
        digits = list(map(int, s))

        @cache
        def dp(index, tight, count):
            if index == N:
                return count
            
            limit = digits[index] if tight else 9
            res = 0

            for digit in range(limit + 1):
                res += dp(index + 1, tight and digit == digits[index], count + 1 if digit == 1 else count)
            
            return res
        
        return dp(0, True, 0)
            

```

