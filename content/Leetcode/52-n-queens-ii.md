---
title: 52. N-Queens II
draft: false
tags: 
  - leetcode-hard
  - backtracking
date: 2022-06-05
---

[Problem Link](https://leetcode.com/problems/n-queens-ii/)

## Description

---
<p>The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an <code>n x n</code> chessboard such that no two queens attack each other.</p>

<p>Given an integer <code>n</code>, return <em>the number of distinct solutions to the&nbsp;<strong>n-queens puzzle</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>Input:</strong> n = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two distinct solutions to the 4-queens puzzle as shown.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>


## Solution

---
### Python
``` py title='n-queens-ii'
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diag1, diag2 = set(), set(), set()
        
        def go(row):
            if row == n: return 1
            
            res = 0
            
            for col in range(n):
                if col not in cols and row - col not in diag1 and row + col not in diag2:
                    cols.add(col)
                    diag1.add(row - col)
                    diag2.add(row + col)
                    res += go(row + 1)
                    cols.remove(col)
                    diag1.remove(row - col)
                    diag2.remove(row + col)
            
            return res
        
        return go(0)
```

