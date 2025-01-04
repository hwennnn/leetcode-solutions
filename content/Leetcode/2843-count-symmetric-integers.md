---
title: 2843.   Count Symmetric Integers
draft: false
tags: 
  - leetcode-easy
  - math
  - enumeration
date: 2023-09-03
---

[Problem Link](https://leetcode.com/problems/count-symmetric-integers/)

## Description

---
<p>You are given two positive integers <code>low</code> and <code>high</code>.</p>

<p>An integer <code>x</code> consisting of <code>2 * n</code> digits is <strong>symmetric</strong> if the sum of the first <code>n</code> digits of <code>x</code> is equal to the sum of the last <code>n</code> digits of <code>x</code>. Numbers with an odd number of digits are never symmetric.</p>

<p>Return <em>the <strong>number of symmetric</strong> integers in the range</em> <code>[low, high]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> low = 1, high = 100
<strong>Output:</strong> 9
<strong>Explanation:</strong> There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> low = 1200, high = 1230
<strong>Output:</strong> 4
<strong>Explanation:</strong> There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= low &lt;= high &lt;= 10<sup>4</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='count-symmetric-integers'
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        
        for i in range(low, high + 1):
            s = str(i)
            N = len(s)
            
            if N >= 2 and N % 2 == 0:
                first = sum(int(x) for x in s[:N // 2])
                last = sum(int(x) for x in s[N // 2:])
                
                if first == last:
                    res += 1
        
        return res
```

