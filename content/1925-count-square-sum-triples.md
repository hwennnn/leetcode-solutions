---
title: 1925. Count Square Sum Triples
draft: false
tags: 
  - leetcode-easy
  - math
  - enumeration
date: 2021-07-11
---

[Problem Link](https://leetcode.com/problems/count-square-sum-triples/)

## Description

---
<p>A <strong>square triple</strong> <code>(a,b,c)</code> is a triple where <code>a</code>, <code>b</code>, and <code>c</code> are <strong>integers</strong> and <code>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></code>.</p>

<p>Given an integer <code>n</code>, return <em>the number of <strong>square triples</strong> such that </em><code>1 &lt;= a, b, c &lt;= n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 2
<strong>Explanation</strong>: The square triples are (3,4,5) and (4,3,5).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 4
<strong>Explanation</strong>: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 250</code></li>
</ul>


## Solution

---
### Python
``` py title='count-square-sum-triples'
class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        mp = collections.defaultdict(int)

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                mp[a * a + b * b] += 1
        
        for c in range(1, n + 1):
            res += mp[c * c]

        
        return res
```
