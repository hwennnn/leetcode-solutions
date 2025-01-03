---
title: 264. Ugly Number II
draft: false
tags: 
  - hash-table
  - math
  - dynamic-programming
  - heap-(priority-queue)
date: 2024-08-18
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
<p>An <strong>ugly number</strong> is a positive integer whose prime factors are limited to <code>2</code>, <code>3</code>, and <code>5</code>.</p>

<p>Given an integer <code>n</code>, return <em>the</em> <code>n<sup>th</sup></code> <em><strong>ugly number</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 12
<strong>Explanation:</strong> [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1690</code></li>
</ul>


## Solution

---
### Python
``` py title='ugly-number-ii'
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        t2 = t3 = t5 = 0
        dp = [1] * n
        
        for i in range(1, n):
            dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            
            if dp[i] == dp[t2] * 2: t2 += 1
            if dp[i] == dp[t3] * 3: t3 += 1
            if dp[i] == dp[t5] * 5: t5 += 1
        
        return dp[-1]

```

