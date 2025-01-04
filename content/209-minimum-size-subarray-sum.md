---
title: 209. Minimum Size Subarray Sum
draft: false
tags: 
  - leetcode-medium
  - array
  - binary-search
  - sliding-window
  - prefix-sum
date: 2023-07-06
---

[Problem Link](https://leetcode.com/problems/minimum-size-subarray-sum/)

## Description

---
<p>Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, return <em>the <strong>minimal length</strong> of a </em><span data-keyword="subarray-nonempty"><em>subarray</em></span><em> whose sum is greater than or equal to</em> <code>target</code>. If there is no such subarray, return <code>0</code> instead.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> target = 7, nums = [2,3,1,2,4,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The subarray [4,3] has the minimal length under the problem constraint.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> target = 4, nums = [1,4,4]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution of which the time complexity is <code>O(n log(n))</code>.

## Solution

---
### Python
``` py title='minimum-size-subarray-sum'
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = inf
        res = INF
        curr = i = 0

        for j, x in enumerate(nums):
            curr += x

            while curr >= target:
                res = min(res, j - i + 1)
                curr -= nums[i]
                i += 1
        
        return res if res != INF else 0
```
