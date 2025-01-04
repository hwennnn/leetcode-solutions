---
title: 343. Integer Break
draft: false
tags: 
  - leetcode-medium
  - math
  - dynamic-programming
date: 2020-08-12
---

[Problem Link](https://leetcode.com/problems/integer-break/)

## Description

---
<p>Given an integer <code>n</code>, break it into the sum of <code>k</code> <strong>positive integers</strong>, where <code>k &gt;= 2</code>, and maximize the product of those integers.</p>

<p>Return <em>the maximum product you can get</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> 2 = 1 + 1, 1 &times; 1 = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 10
<strong>Output:</strong> 36
<strong>Explanation:</strong> 10 = 3 + 3 + 4, 3 &times; 3 &times; 4 = 36.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 58</code></li>
</ul>


## Solution

---
### Python
``` py title='integer-break'
class Solution:
    def integerBreak(self, n: int) -> int:
        # 2 -> 1
        # 3 -> (1, 2)
        # 4 -> 4
        # 5 -> (3, 2) better than (4, 1)
        # 6 -> (3, 3) better than (4, 2)
        # 7 -> (4, 3) better than (3, 3, 1)
        # 8 -> (3. 3. 2) better than (4, 3)
        # 9 -> (3, 3, 3) better than (5, 4)

        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4

        res = 1
        while n > 4:
            res *= 3
            n -= 3
        
        res *= n

        return res
```
### C++
``` cpp title='integer-break'
class Solution {
public:
    int integerBreak(int n) {
        if(n==2)    return 1;
        if(n==3)    return 2;
        
        int res = 1;
        
        while (n > 4){
            res *= 3;
            n -= 3;
        }
            
        res *= n;
        
        return res;
    }
};
```

