---
title: 907. Sum of Subarray Minimums
draft: false
tags: 
  - leetcode-medium
  - array
  - dynamic-programming
  - stack
  - monotonic-stack
date: 2024-01-21
---

[Problem Link](https://leetcode.com/problems/sum-of-subarray-minimums/)

## Description

---
<p>Given an array of integers arr, find the sum of <code>min(b)</code>, where <code>b</code> ranges over every (contiguous) subarray of <code>arr</code>. Since the answer may be large, return the answer <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [3,1,2,4]
<strong>Output:</strong> 17
<strong>Explanation:</strong> 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [11,81,94,43,3]
<strong>Output:</strong> 444
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 3 * 10<sup>4</sup></code></li>
</ul>


## Solution

---
### Python3
``` py title='sum-of-subarray-minimums'
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)
        res = 0
        M = 10 ** 9 + 7

        left = []
        stack = []
        for i, x in enumerate(arr):
            while stack and x < arr[stack[-1]]:
                stack.pop()
            
            if stack:
                left.append(i - stack[-1])
            else:
                left.append(i + 1)
            
            stack.append(i)
        
        right = []
        stack = []
        for i in range(N - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            
            if stack:
                right.append(stack[-1] - i)
            else:
                right.append(N - i)
            
            stack.append(i)
        right.reverse()
        
        for i, x in enumerate(arr):
            res += x * left[i] * right[i]
            res %= M
        
        return res
```

