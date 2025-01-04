---
title: 16. 3Sum Closest
draft: false
tags: 
  - leetcode-medium
  - array
  - two-pointers
  - sorting
date: 2022-10-08
---

[Problem Link](https://leetcode.com/problems/3sum-closest/)

## Description

---
<p>Given an integer array <code>nums</code> of length <code>n</code> and an integer <code>target</code>, find three integers in <code>nums</code> such that the sum is closest to <code>target</code>.</p>

<p>Return <em>the sum of the three integers</em>.</p>

<p>You may assume that each input would have exactly one solution.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,2,1,-4], target = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,0,0], target = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


## Solution

---
### Python3
``` py title='3sum-closest'
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        nums.sort()
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == target:
                    return s
                elif s > target:
                    k -= 1
                else:
                    j += 1
                
                if abs(s - target) < abs(res - target):
                    res = s
        
        return res
```

