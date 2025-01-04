---
title: 119. Pascal's Triangle II
draft: false
tags: 
  - leetcode-easy
  - array
  - dynamic-programming
date: 2020-08-16
---

[Problem Link](https://leetcode.com/problems/pascals-triangle-ii/)

## Description

---
<p>Given an integer <code>rowIndex</code>, return the <code>rowIndex<sup>th</sup></code> (<strong>0-indexed</strong>) row of the <strong>Pascal&#39;s triangle</strong>.</p>

<p>In <strong>Pascal&#39;s triangle</strong>, each number is the sum of the two numbers directly above it as shown:</p>
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height:240px; width:260px" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> rowIndex = 3
<strong>Output:</strong> [1,3,3,1]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> rowIndex = 0
<strong>Output:</strong> [1]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> rowIndex = 1
<strong>Output:</strong> [1,1]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= rowIndex &lt;= 33</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you optimize your algorithm to use only <code>O(rowIndex)</code> extra space?</p>


## Solution

---
### Python3
``` py title='pascals-triangle-ii'
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t = [[1], [1, 1]]
        
        for index in range(2, rowIndex + 1):
            tt = t[-1]
            tmp = [1] + [0] * (index - 1) + [1]
            for i in range(1, len(tmp) - 1):
                left = tt[i - 1]
                right = tt[-1] if i + 1 >= len(tt) else tt[i]
                tmp[i] = left + right
            
            t.append(tmp)
        
        return t[rowIndex]
```
### C++
``` cpp title='pascals-triangle-ii'
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        int n = rowIndex+1;
        vector<int> tri(n,0);
        tri[0] = 1;
        
        
        for (int i = 1; i < n; i++){
             for (int j = i; j > 0; j--){
                 tri[j] += tri[j-1];
             }
        }
           
                
        
        return tri;
        
    }
};
```

