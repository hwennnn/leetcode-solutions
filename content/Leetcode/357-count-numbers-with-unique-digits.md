---
title: 357. Count Numbers with Unique Digits
draft: false
tags: 
  - math
  - dynamic-programming
  - backtracking
date: 2022-09-06
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
<p>Given an integer <code>n</code>, return the count of all numbers with unique digits, <code>x</code>, where <code>0 &lt;= x &lt; 10<sup>n</sup></code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 91
<strong>Explanation:</strong> The answer should be the total numbers in the range of 0 &le; x &lt; 100, excluding 11,22,33,44,55,66,77,88,99
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 8</code></li>
</ul>


## Solution

---
### Python
``` py title='count-numbers-with-unique-digits'
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        
        n = (10 ** n) - 1
        digits = []
        
        while n > 0:
            digits.append(n % 10)
            n //= 10
        
        digits.reverse()
        N = len(digits)
        
        @cache
        def dp(pos, tight, mask):
            if pos == N:
                return 1
            
            limit = digits[pos] if tight else 9
            res = 0
            
            for i in range(0, limit + 1):
                if mask & (1 << i) > 0: continue
                    
                nextTight = tight and i == digits[pos]
                nextMask = mask if i == 0 and mask == 0 else mask ^ (1 << i)
                
                res += dp(pos + 1, nextTight, nextMask)
            
            return res
        
        return dp(0, True, 0)

```

