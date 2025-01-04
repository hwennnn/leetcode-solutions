---
title: 1879. Minimum XOR Sum of Two Arrays
draft: false
tags: 
  - leetcode-hard
  - array
  - dynamic-programming
  - bit-manipulation
  - bitmask
date: 2022-01-04
---

[Problem Link](https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/)

## Description

---
<p>You are given two integer arrays <code>nums1</code> and <code>nums2</code> of length <code>n</code>.</p>

<p>The <strong>XOR sum</strong> of the two integer arrays is <code>(nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1])</code> (<strong>0-indexed</strong>).</p>

<ul>
	<li>For example, the <strong>XOR sum</strong> of <code>[1,2,3]</code> and <code>[3,2,1]</code> is equal to <code>(1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4</code>.</li>
</ul>

<p>Rearrange the elements of <code>nums2</code> such that the resulting <strong>XOR sum</strong> is <b>minimized</b>.</p>

<p>Return <em>the <strong>XOR sum</strong> after the rearrangement</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2], nums2 = [2,3]
<strong>Output:</strong> 2
<b>Explanation:</b> Rearrange <code>nums2</code> so that it becomes <code>[3,2]</code>.
The XOR sum is (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,0,3], nums2 = [5,3,4]
<strong>Output:</strong> 8
<b>Explanation:</b> Rearrange <code>nums2</code> so that it becomes <code>[5,4,3]</code>. 
The XOR sum is (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length</code></li>
	<li><code>n == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 14</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='minimum-xor-sum-of-two-arrays'
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @cache
        def dp(i, mask):
            if i == n: return 0
            
            res = float('inf')
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    res = min(res, dp(i + 1, mask ^ (1 << j)) + (nums1[i] ^ nums2[j]))
                
            return res
        
        return dp(0, (1 << n) - 1)
```
