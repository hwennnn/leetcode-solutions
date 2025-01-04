---
title: 2470. Number of Subarrays With LCM Equal to K
draft: false
tags: 
  - leetcode-medium
  - array
  - math
  - number-theory
date: 2022-11-13
---

[Problem Link](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/)

## Description

---
<p>Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the number of <strong>subarrays</strong> of </em><code>nums</code><em> where the least common multiple of the subarray&#39;s elements is </em><code>k</code>.</p>

<p>A <strong>subarray</strong> is a contiguous non-empty sequence of elements within an array.</p>

<p>The <strong>least common multiple of an array</strong> is the smallest positive integer that is divisible by all the array elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,6,2,7,1], k = 6
<strong>Output:</strong> 4
<strong>Explanation:</strong> The subarrays of nums where 6 is the least common multiple of all the subarray&#39;s elements are:
- [<u><strong>3</strong></u>,<u><strong>6</strong></u>,2,7,1]
- [<u><strong>3</strong></u>,<u><strong>6</strong></u>,<u><strong>2</strong></u>,7,1]
- [3,<u><strong>6</strong></u>,2,7,1]
- [3,<u><strong>6</strong></u>,<u><strong>2</strong></u>,7,1]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3], k = 2
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no subarrays of nums where 2 is the least common multiple of all the subarray&#39;s elements.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 1000</code></li>
</ul>


## Solution

---
### Python
``` py title='number-of-subarrays-with-lcm-equal-to-k'
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            l = nums[i]
            
            for j in range(i, N):
                l = lcm(l, nums[j])
                
                if l > k: break
                
                if l == k:
                    res += 1
        
        return res
                
        
        
```
