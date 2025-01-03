---
title: 282. Expression Add Operators
draft: false
tags: 
  - math
  - string
  - backtracking
date: 2021-09-18
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>Given a string <code>num</code> that contains only digits and an integer <code>target</code>, return <em><strong>all possibilities</strong> to insert the binary operators </em><code>&#39;+&#39;</code><em>, </em><code>&#39;-&#39;</code><em>, and/or </em><code>&#39;*&#39;</code><em> between the digits of </em><code>num</code><em> so that the resultant expression evaluates to the </em><code>target</code><em> value</em>.</p>

<p>Note that operands in the returned expressions <strong>should not</strong> contain leading zeros.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;123&quot;, target = 6
<strong>Output:</strong> [&quot;1*2*3&quot;,&quot;1+2+3&quot;]
<strong>Explanation:</strong> Both &quot;1*2*3&quot; and &quot;1+2+3&quot; evaluate to 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;232&quot;, target = 8
<strong>Output:</strong> [&quot;2*3+2&quot;,&quot;2+3*2&quot;]
<strong>Explanation:</strong> Both &quot;2*3+2&quot; and &quot;2+3*2&quot; evaluate to 8.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = &quot;3456237490&quot;, target = 9191
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no expressions that can be created from &quot;3456237490&quot; to evaluate to 9191.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10</code></li>
	<li><code>num</code> consists of only digits.</li>
	<li><code>-2<sup>31</sup> &lt;= target &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## Solution

---
### Python
``` py title='expression-add-operators'
class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        n = len(s)
        res = []
        
        def backtrack(i, path, curr, prev):
            if i == n:
                if curr == target:
                    res.append(path)
                return
            
            for j in range(i, n):
                if j > i and s[i] == '0': break
                num = int(s[i : j + 1])
                
                if i == 0:
                    backtrack(j + 1, path + str(num), curr + num, num)
                else:
                    backtrack(j + 1, path + "+" + str(num), curr + num, num)
                    backtrack(j + 1, path + "-" + str(num), curr - num, -num)
                    backtrack(j + 1, path + "*" + str(num), curr - prev + prev * num, prev * num)
                    
        backtrack(0, "", 0, 0)
        return res

```

