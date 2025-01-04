---
title: 22. Generate Parentheses
draft: false
tags: 
  - leetcode-medium
  - string
  - dynamic-programming
  - backtracking
date: 2021-09-05
---

[Problem Link](https://leetcode.com/problems/generate-parentheses/)

## Description

---
<p>Given <code>n</code> pairs of parentheses, write a function to <em>generate all combinations of well-formed parentheses</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> ["((()))","(()())","(())()","()(())","()()()"]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> ["()"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 8</code></li>
</ul>


## Solution

---
### Python
``` py title='generate-parentheses'
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(opened, closed, curr):
            if opened == closed == n:
                res.append(curr)
                return
            
            if closed < opened:
                backtrack(opened, closed + 1, curr + ")")
            
            if opened < n:
                backtrack(opened + 1, closed, curr + "(")
            
        backtrack(0, 0, "")
        return res
```

