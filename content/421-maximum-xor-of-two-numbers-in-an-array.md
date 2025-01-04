---
title: 421. Maximum XOR of Two Numbers in an Array
draft: false
tags: 
  - leetcode-medium
  - array
  - hash-table
  - bit-manipulation
  - trie
date: 2023-11-12
---

[Problem Link](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

## Description

---
<p>Given an integer array <code>nums</code>, return <em>the maximum result of </em><code>nums[i] XOR nums[j]</code>, where <code>0 &lt;= i &lt;= j &lt; n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,10,5,25,2,8]
<strong>Output:</strong> 28
<strong>Explanation:</strong> The maximum result is 5 XOR 25 = 28.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [14,70,53,83,49,91,36,80,92,51,66,70]
<strong>Output:</strong> 127
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## Solution

---
### Python3
``` py title='maximum-xor-of-two-numbers-in-an-array'
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        N = len(nums)
        MAX_BIT = max(nums).bit_length()
        root = [None, None]
        res = 0

        def add(x):
            curr = root

            for k in range(MAX_BIT, -1, -1):
                if x & (1 << k) > 0:
                    bit = 1
                else:
                    bit = 0
                
                if curr[bit] is None:
                    curr[bit] = [None, None]
                
                curr = curr[bit]
        
        def query(x):
            res = 0
            curr = root

            for k in range(MAX_BIT, -1, -1):
                if x & (1 << k) > 0:
                    bit = 1
                else:
                    bit = 0

                opp = 1 - bit

                if curr is not None and curr[opp] is not None:
                    res += (1 << k)
                    curr = curr[opp]
                else:
                    if curr is None:
                        curr = [None, None]
                    curr = curr[bit]

            return res

        for x in nums:
            res = max(res, query(x))
            add(x)
        
        return res
```

