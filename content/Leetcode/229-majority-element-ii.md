---
title: 229. Majority Element II
draft: false
tags: 
  - leetcode-medium
  - array
  - hash-table
  - sorting
  - counting
date: 2023-10-05
---

[Problem Link](https://leetcode.com/problems/majority-element-ii/)

## Description

---
<p>Given an integer array of size <code>n</code>, find all elements that appear more than <code>&lfloor; n/3 &rfloor;</code> times.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,3]
<strong>Output:</strong> [3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1]
<strong>Output:</strong> [1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?</p>


## Solution

---
### Python
``` py title='majority-element-ii'
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        maj1, maj2, count1, count2 = None, None, 0, 0

        for x in nums:
            if x == maj1:
                count1 += 1
            elif x == maj2:
                count2 += 1
            elif count1 == 0:
                maj1, count1 = x, 1
            elif count2 == 0:
                maj2, count2 = x, 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [maj for maj in (maj1, maj2) if nums.count(maj) > N // 3]
```

