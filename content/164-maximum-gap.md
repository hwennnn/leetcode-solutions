---
title: 164. Maximum Gap
draft: false
tags: 
  - leetcode-medium
  - array
  - sorting
  - bucket-sort
  - radix-sort
date: 2021-05-30
---

[Problem Link](https://leetcode.com/problems/maximum-gap/)

## Description

---
<p>Given an integer array <code>nums</code>, return <em>the maximum difference between two successive elements in its sorted form</em>. If the array contains less than two elements, return <code>0</code>.</p>

<p>You must write an algorithm that runs in linear time and uses linear extra space.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,6,9,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The array contains less than 2 elements, therefore return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## Solution

---
### Python3
``` py title='maximum-gap'
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        
        mmax, mmin = float('-inf'), float('inf')
        
        for num in nums:
            mmax = max(mmax, num)
            mmin = min(mmin, num)
        
        gap = math.ceil((mmax - mmin) / (n - 1)) or 1
        bucket_max = [float('-inf') for _ in range(n)]
        bucket_min = [float('inf') for _ in range(n)]
        
        for num in nums:
            index = (num - mmin) // gap
            bucket_max[index] = max(bucket_max[index], num)
            bucket_min[index] = min(bucket_min[index], num)

        maxGap = float('-inf')
        prevMax = mmin
        
        for i in range(n):
            if bucket_max[i] == float('-inf') and bucket_min[i] == float('inf'): continue
            
            maxGap = max(maxGap, bucket_min[i] - prevMax)
            prevMax = bucket_max[i]
        
        return maxGap
```

