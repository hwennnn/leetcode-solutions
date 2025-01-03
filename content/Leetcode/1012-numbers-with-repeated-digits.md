---
title: 1012. Numbers With Repeated Digits
draft: false
tags: 
  - math
  - dynamic-programming
date: 2022-09-06
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>Given an integer <code>n</code>, return <em>the number of positive integers in the range </em><code>[1, n]</code><em> that have <strong>at least one</strong> repeated digit</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 20
<strong>Output:</strong> 1
<strong>Explanation:</strong> The only positive number (&lt;= 20) with at least 1 repeated digit is 11.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 100
<strong>Output:</strong> 10
<strong>Explanation:</strong> The positive numbers (&lt;= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1000
<strong>Output:</strong> 262
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='numbers-with-repeated-digits'
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        
        def findNonRepeated(n):
            digits = []

            while n > 0:
                digits.append(n % 10)
                n //= 10

            digits.reverse()

            N = len(digits)

            @cache
            def dp(pos, tight, mask):
                if pos == N:
                    return 1 if mask != 0 else 0

                limit = digits[pos] if tight else 9
                res = 0

                for i in range(0, limit + 1):
                    if mask & (1 << i) > 0: continue

                    nextTight = tight and i == digits[pos]
                    nextMask = mask if i == 0 and mask == 0 else mask ^ (1 << i)

                    res += dp(pos + 1, nextTight, nextMask)

                return res
            
            return dp(0, True, 0)
        
        return n - findNonRepeated(n)

```

