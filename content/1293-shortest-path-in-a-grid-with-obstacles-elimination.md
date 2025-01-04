---
title: 1293. Shortest Path in a Grid with Obstacles Elimination
draft: false
tags: 
  - leetcode-hard
  - array
  - breadth-first-search
  - matrix
date: 2022-10-30
---

[Problem Link](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/)

## Description

---
<p>You are given an <code>m x n</code> integer matrix <code>grid</code> where each cell is either <code>0</code> (empty) or <code>1</code> (obstacle). You can move up, down, left, or right from and to an empty cell in <strong>one step</strong>.</p>

<p>Return <em>the minimum number of <strong>steps</strong> to walk from the upper left corner </em><code>(0, 0)</code><em> to the lower right corner </em><code>(m - 1, n - 1)</code><em> given that you can eliminate <strong>at most</strong> </em><code>k</code><em> obstacles</em>. If it is not possible to find such walk return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/30/short1-grid.jpg" style="width: 244px; height: 405px;" />
<pre>
<strong>Input:</strong> grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> 
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -&gt; (0,1) -&gt; (0,2) -&gt; (1,2) -&gt; (2,2) -&gt; <strong>(3,2)</strong> -&gt; (4,2).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/30/short2-grid.jpg" style="width: 244px; height: 245px;" />
<pre>
<strong>Input:</strong> grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
<strong>Output:</strong> -1
<strong>Explanation:</strong> We need to eliminate at least two obstacles to find such a walk.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 40</code></li>
	<li><code>1 &lt;= k &lt;= m * n</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> <strong>or</strong> <code>1</code>.</li>
	<li><code>grid[0][0] == grid[m - 1][n - 1] == 0</code></li>
</ul>


## Solution

---
### Python
``` py title='shortest-path-in-a-grid-with-obstacles-elimination'
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque([(0, 0, 0, k)])
        visited = set([(0, 0, k)])
        
        while queue:
            x, y, steps, skip = queue.popleft()

            if x == rows - 1 and y == cols - 1:
                return steps
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols:
                    if grid[dx][dy] == 0 and (dx, dy, skip) not in visited:
                        queue.append((dx, dy, steps + 1, skip))
                        visited.add((dx, dy, skip))
                    elif grid[dx][dy] == 1 and skip >= 1 and (dx, dy, skip - 1) not in visited:
                        queue.append((dx, dy, steps + 1, skip - 1))
                        visited.add((dx, dy, skip - 1))
            
        return -1
```
