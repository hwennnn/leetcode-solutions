---
title: 2099. Find Subsequence of Length K With the Largest Sum
draft: false
tags: 
  - leetcode-easy
  - array
  - hash-table
  - sorting
  - heap-priority-queue
date: 2021-12-11
---

[Problem Link](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)

## Description

---
<p>You are given an integer array <code>nums</code> and an integer <code>k</code>. You want to find a <strong>subsequence </strong>of <code>nums</code> of length <code>k</code> that has the <strong>largest</strong> sum.</p>

<p>Return<em> </em><em><strong>any</strong> such subsequence as an integer array of length </em><code>k</code>.</p>

<p>A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,1,3,3], k = 2
<strong>Output:</strong> [3,3]
<strong>Explanation:</strong>
The subsequence has the largest sum of 3 + 3 = 6.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-1,-2,3,4], k = 3
<strong>Output:</strong> [-1,3,4]
<strong>Explanation:</strong> 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,4,3,3], k = 2
<strong>Output:</strong> [3,4]
<strong>Explanation:</strong>
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## Solution

---
### Python
``` py title='find-subsequence-of-length-k-with-the-largest-sum'
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = set(list(range(k)))
        heap = [(x, i) for i, x in enumerate(nums[:k])]
        heapq.heapify(heap) 

        for i, x in enumerate(nums[k:], k):
            res.add(i)
            value, index = heapq.heappushpop(heap, (x, i))
            res.remove(index)
            
        
        return [nums[i] for i in sorted(list(res))]
```

