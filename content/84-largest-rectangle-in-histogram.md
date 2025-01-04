---
title: 84. Largest Rectangle in Histogram
draft: false
tags: 
  - leetcode-hard
  - array
  - stack
  - monotonic-stack
date: 2023-08-22
---

[Problem Link](https://leetcode.com/problems/largest-rectangle-in-histogram/)

## Description

---
<p>Given an array of integers <code>heights</code> representing the histogram&#39;s bar height where the width of each bar is <code>1</code>, return <em>the area of the largest rectangle in the histogram</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" style="width: 522px; height: 242px;" />
<pre>
<strong>Input:</strong> heights = [2,1,5,6,2,3]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" style="width: 202px; height: 362px;" />
<pre>
<strong>Input:</strong> heights = [2,4]
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= heights.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= heights[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## Solution

---
### Python3
``` py title='largest-rectangle-in-histogram'
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        lessFromLeft = [0] * N
        lessFromRight = [0] * N
        lessFromLeft[0] = -1
        lessFromRight[-1] = N

        for i in range(1, N):
            p = i - 1

            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            
            lessFromLeft[i] = p
        
        for i in range(N - 2, -1, -1):
            p = i + 1

            while p < N and heights[p] >= heights[i]:
                p = lessFromRight[p]
            
            lessFromRight[i] = p
        
        res = 0
        for i in range(N):
            res = max(res, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))
        
        return res
```

