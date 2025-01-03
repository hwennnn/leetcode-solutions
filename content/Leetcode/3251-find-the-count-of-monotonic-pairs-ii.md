---
title: 3251. Find the Count of Monotonic Pairs II
draft: false
tags: 
  - array
  - math
  - dynamic-programming
  - combinatorics
  - prefix-sum
date: 2024-08-14
---

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-blue.svg)

## Description

---
<p>You are given an array of <strong>positive</strong> integers <code>nums</code> of length <code>n</code>.</p>

<p>We call a pair of <strong>non-negative</strong> integer arrays <code>(arr1, arr2)</code> <strong>monotonic</strong> if:</p>

<ul>
	<li>The lengths of both arrays are <code>n</code>.</li>
	<li><code>arr1</code> is monotonically <strong>non-decreasing</strong>, in other words, <code>arr1[0] &lt;= arr1[1] &lt;= ... &lt;= arr1[n - 1]</code>.</li>
	<li><code>arr2</code> is monotonically <strong>non-increasing</strong>, in other words, <code>arr2[0] &gt;= arr2[1] &gt;= ... &gt;= arr2[n - 1]</code>.</li>
	<li><code>arr1[i] + arr2[i] == nums[i]</code> for all <code>0 &lt;= i &lt;= n - 1</code>.</li>
</ul>

<p>Return the count of <strong>monotonic</strong> pairs.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The good pairs are:</p>

<ol>
	<li><code>([0, 1, 1], [2, 2, 1])</code></li>
	<li><code>([0, 1, 2], [2, 2, 0])</code></li>
	<li><code>([0, 2, 2], [2, 1, 0])</code></li>
	<li><code>([1, 2, 2], [1, 1, 0])</code></li>
</ol>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,5,5,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">126</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 2000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Solution

---
### Python
``` py title='find-the-count-of-monotonic-pairs-ii'
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        N = len(nums)
        M = 10 ** 9 + 7
        dp = [[0] * 1001 for _ in range(N)] # dp[index][amount]

        # curr >= prev && (nums[i] - curr) <= (nums[i-1] - prev)
        # prev <= curr && prev <= curr - nums[i] + nums[i - 1]
        # simplify => prev <= min(curr, curr - nums[i] + nums[i - 1])
        # so, prev <= min(curr, curr - nums[i] + nums[i - 1])
        # and when prev increases by 1, prev + 1 <= min(curr + 1, curr + 1 - nums[i] + nums[i - 1])
        # and it can be seen that the difference is only one, hence can use prefix sum to compute that

        for j in range(nums[0] + 1):
            dp[0][j] = 1

        for i in range(1, N):
            ways = 0
            prev = 0

            for curr in range(nums[i] + 1):
                if prev <= min(curr, curr - nums[i] + nums[i - 1]):
                    ways += dp[i - 1][prev]
                    ways %= M
                    prev += 1
            
                dp[i][curr] = ways
        
        res = 0
        for curr in range(1001):
            res += dp[N - 1][curr]
            res %= M

        return res

```

