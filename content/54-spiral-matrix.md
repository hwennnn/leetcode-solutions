---
title: 54. Spiral Matrix
draft: false
tags: 
  - leetcode-medium
  - array
  - matrix
  - simulation
date: 2023-05-09
---

[Problem Link](https://leetcode.com/problems/spiral-matrix/)

## Description

---
<p>Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the</em> <code>matrix</code> <em>in spiral order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3],[4,5,6],[7,8,9]]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10</code></li>
	<li><code>-100 &lt;= matrix[i][j] &lt;= 100</code></li>
</ul>


## Solution

---
### Python3
``` py title='spiral-matrix'
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows, cols = len(matrix), len(matrix[0])
        rowStart, rowEnd = 0, rows - 1
        colStart, colEnd = 0, cols - 1
        
        while len(res) < rows * cols:
            # traverse right
            i = colStart
            while len(res) < rows * cols and i <= colEnd:
                res.append(matrix[rowStart][i])
                i += 1
            rowStart += 1
            
            # traverse down
            i = rowStart
            while len(res) < rows * cols and i <= rowEnd:
                res.append(matrix[i][colEnd])
                i += 1
            colEnd -= 1
            
            # traverse left
            i = colEnd
            while len(res) < rows * cols and i >= colStart:
                res.append(matrix[rowEnd][i])
                i -= 1
            rowEnd -= 1
        
            # traverse up
            i = rowEnd
            while len(res) < rows * cols and i >= rowStart:
                res.append(matrix[i][colStart])
                i -= 1
            colStart += 1
                
        
        return res
```

