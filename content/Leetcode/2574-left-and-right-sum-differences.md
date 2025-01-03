---
title: 2574. Left and Right Sum Differences
draft: false
tags: 
  - array
  - prefix-sum
date: 2023-02-26
---

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-blue.svg)

## Description

---
<p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, find a <strong>0-indexed </strong>integer array <code>answer</code> where:</p>

<ul>
    <li><code>answer.length == nums.length</code>.</li>
    <li><code>answer[i] = |leftSum[i] - rightSum[i]|</code>.</li>
</ul>

<p>Where:</p>

<ul>
    <li><code>leftSum[i]</code> is the sum of elements to the left of the index <code>i</code> in the array <code>nums</code>. If there is no such element, <code>leftSum[i] = 0</code>.</li>
    <li><code>rightSum[i]</code> is the sum of elements to the right of the index <code>i</code> in the array <code>nums</code>. If there is no such element, <code>rightSum[i] = 0</code>.</li>
</ul>

<p>Return <em>the array</em> <code>answer</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,4,8,3]
<strong>Output:</strong> [15,1,11,22]
<strong>Explanation:</strong> The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [0]
<strong>Explanation:</strong> The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='left-and-right-sum-differences'
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        res = []
        
        for x in nums:            
            right -= x
            
            res.append(abs(left - right))
            
            left += x
            
        return res
        

```

