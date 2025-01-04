---
title: 179. Largest Number
draft: false
tags: 
  - leetcode-medium
  - array
  - string
  - greedy
  - sorting
date: 2020-09-25
---

[Problem Link](https://leetcode.com/problems/largest-number/)

## Description

---
<p>Given a list of non-negative integers <code>nums</code>, arrange them such that they form the largest number and return it.</p>

<p>Since the result may be very large, so you need to return a string instead of an integer.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,2]
<strong>Output:</strong> &quot;210&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,30,34,5,9]
<strong>Output:</strong> &quot;9534330&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='largest-number'
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(nums):
            return "0"
            
        def compare(a, b):
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0   # a and b are equal

        s = list(map(str, nums))
        s.sort(key = cmp_to_key(compare))
        return "".join(s)
```
### Python
``` py title='largest-number'
import functools 

class Solution:
    def largestNumber(self, nums):
        compare = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        _nums = list(map(str, nums))
        _nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        return str(int(''.join(_nums)))
```

