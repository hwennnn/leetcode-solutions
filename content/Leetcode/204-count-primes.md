---
title: 204. Count Primes
draft: false
tags: 
  - array
  - math
  - enumeration
  - number-theory
date: 2021-05-10
---

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-blue.svg)

## Description

---
<p>Given an integer <code>n</code>, return <em>the number of prime numbers that are strictly less than</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 0
<strong>Output:</strong> 0
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 5 * 10<sup>6</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='count-primes'
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        
        arr = [True] * n
        arr[0] = arr[1] = False
        
        for i in range(2, n):
            if arr[i]:
                for j in range(i * i, n, i):
                    arr[j] = False
        
        return sum(arr)

```

