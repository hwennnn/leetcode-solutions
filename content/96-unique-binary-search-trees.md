---
title: 96. Unique Binary Search Trees
draft: false
tags: 
  - leetcode-medium
  - math
  - dynamic-programming
  - tree
  - binary-search-tree
  - binary-tree
date: 2021-11-08
---

[Problem Link](https://leetcode.com/problems/unique-binary-search-trees/)

## Description

---
<p>Given an integer <code>n</code>, return <em>the number of structurally unique <strong>BST&#39;</strong>s (binary search trees) which has exactly </em><code>n</code><em> nodes of unique values from</em> <code>1</code> <em>to</em> <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 5
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 19</code></li>
</ul>


## Solution

---
### Python3
``` py title='unique-binary-search-trees'
class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def go(n):
            if n == 0: return 0
            if n == 1: return 1
            
            res = 0
            for head in range(n):
                res += max(1, go(head)) * max(1, go(n - head - 1))
            
            return res
        
        return go(n)
```

