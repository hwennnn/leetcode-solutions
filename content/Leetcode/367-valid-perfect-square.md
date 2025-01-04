---
title: 367. Valid Perfect Square
draft: false
tags: 
  - leetcode-easy
  - math
  - binary-search
date: 2022-05-14
---

[Problem Link](https://leetcode.com/problems/valid-perfect-square/)

## Description

---
<p>Given a positive integer num, return <code>true</code> <em>if</em> <code>num</code> <em>is a perfect square or</em> <code>false</code> <em>otherwise</em>.</p>

<p>A <strong>perfect square</strong> is an integer that is the square of an integer. In other words, it is the product of some integer with itself.</p>

<p>You must not use any built-in library function, such as <code>sqrt</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 16
<strong>Output:</strong> true
<strong>Explanation:</strong> We return true because 4 * 4 = 16 and 4 is an integer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 14
<strong>Output:</strong> false
<strong>Explanation:</strong> We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## Solution

---
### Python
``` py title='valid-perfect-square'
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, 10 ** 18
        
        while left < right:
            mid = left + (right - left) // 2
            
            if mid * mid >= num:
                right = mid
            else:
                left = mid + 1
        
        return left * left == num
```

