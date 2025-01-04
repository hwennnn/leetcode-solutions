---
title: 137. Single Number II
draft: false
tags: 
  - leetcode-medium
  - array
  - bit-manipulation
date: 2023-07-04
---

[Problem Link](https://leetcode.com/problems/single-number-ii/)

## Description

---
<p>Given an integer array <code>nums</code> where&nbsp;every element appears <strong>three times</strong> except for one, which appears <strong>exactly once</strong>. <em>Find the single element and return it</em>.</p>

<p>You must&nbsp;implement a solution with a linear runtime complexity and use&nbsp;only constant&nbsp;extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,2,3,2]
<strong>Output:</strong> 3
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0,1,0,1,0,1,99]
<strong>Output:</strong> 99
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>Each element in <code>nums</code> appears exactly <strong>three times</strong> except for one element which appears <strong>once</strong>.</li>
</ul>


## Solution

---
### Python
``` py title='single-number-ii'
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32

        for x in nums:
            for i in range(32):
                if (x >> i) & 1 == 1:
                    bits[i] += 1
                    bits[i] %= 3
        
        res = 0
        for i in range(32):
            if bits[i]:
                res |= (1 << i)
        
        if res & 1 << 31:
            res -= 2 ** 32

        return res
```

