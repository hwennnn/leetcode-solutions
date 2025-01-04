---
title: 59. Spiral Matrix II
draft: false
tags: 
  - leetcode-medium
  - array
  - matrix
  - simulation
date: 2023-05-10
---

[Problem Link](https://leetcode.com/problems/spiral-matrix-ii/)

## Description

---
<p>Given a positive integer <code>n</code>, generate an <code>n x n</code> <code>matrix</code> filled with elements from <code>1</code> to <code>n<sup>2</sup></code> in spiral order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> [[1,2,3],[8,9,4],[7,6,5]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> [[1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
</ul>


## Solution

---
### Python
``` py title='spiral-matrix-ii'
class Solution:
    def generateMatrix(self, n):
        res, lo = [[n*n]], n*n 
        while lo > 1:
            lo, hi = lo - len(res), lo
            #print('res:', res)
            res = [[i for i in range(lo, hi)]] + [list(j) for j in zip(*res[::-1])]
        return res
```

