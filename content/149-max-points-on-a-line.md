---
title: 149. Max Points on a Line
draft: false
tags: 
  - leetcode-hard
  - array
  - hash-table
  - math
  - geometry
date: 2023-01-08
---

[Problem Link](https://leetcode.com/problems/max-points-on-a-line/)

## Description

---
<p>Given an array of <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents a point on the <strong>X-Y</strong> plane, return <em>the maximum number of points that lie on the same straight line</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[2,2],[3,3]]
<strong>Output:</strong> 3
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg" style="width: 300px; height: 294px;" />
<pre>
<strong>Input:</strong> points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 300</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li>All the <code>points</code> are <strong>unique</strong>.</li>
</ul>


## Solution

---
### Python3
``` py title='max-points-on-a-line'
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        INT_MAX = 10 ** 5
        
        for i in range(n):
            x1, y1 = points[i]
            mp = collections.defaultdict(int)
            samePoints = 1
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    samePoints += 1
                elif x1 == x2:
                    mp[INT_MAX] += 1
                else:
                    x, y = x2 - x1, y2 - y1
                    divisor = gcd(x, y)
                    x, y = x // divisor, y // divisor
                    mp[y / x] += 1

            mmax = max(mp.values() or [0])
            mmax += samePoints
            res = max(res, mmax)
                    
        return res
```

