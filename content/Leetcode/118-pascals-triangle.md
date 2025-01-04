---
title: 118. Pascal's Triangle
draft: false
tags: 
  - leetcode-easy
  - array
  - dynamic-programming
date: 2020-08-12
---

[Problem Link](https://leetcode.com/problems/pascals-triangle/)

## Description

---
<p>Given an integer <code>numRows</code>, return the first numRows of <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> numRows = 5
<strong>Output:</strong> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> numRows = 1
<strong>Output:</strong> [[1]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= numRows &lt;= 30</code></li>
</ul>


## Solution

---
### Python
``` py title='pascals-triangle'
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        A = [[1] * (i + 1) for i in range(numRows)]
        
        for row in range(2, numRows):
            for j in range(1, len(A[row]) - 1):
                A[row][j] = A[row - 1][j - 1] + A[row - 1][j]
        
        return A
```
### Java
``` java title='pascals-triangle'
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        ArrayList<Integer> pre = null;
        for (int i = 1; i <= numRows; i++) {
            ArrayList<Integer> save = new ArrayList<>();
            for (int j = 1; j <= i; j++)
                if (j == 1 || j == i) save.add(1);
                else save.add(pre.get(j-1) + pre.get(j-2));
            result.add(save);
            pre = save;
        }
        return result;
    }
}
```

