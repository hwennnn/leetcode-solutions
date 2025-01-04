---
title: 2709. Greatest Common Divisor Traversal
draft: false
tags: 
  - leetcode-hard
  - array
  - math
  - union-find
  - number-theory
date: 2024-02-25
---

[Problem Link](https://leetcode.com/problems/greatest-common-divisor-traversal/)

## Description

---
<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>, and you are allowed to <strong>traverse</strong> between its indices. You can traverse between index <code>i</code> and index <code>j</code>, <code>i != j</code>, if and only if <code>gcd(nums[i], nums[j]) &gt; 1</code>, where <code>gcd</code> is the <strong>greatest common divisor</strong>.</p>

<p>Your task is to determine if for <strong>every pair</strong> of indices <code>i</code> and <code>j</code> in nums, where <code>i &lt; j</code>, there exists a <strong>sequence of traversals</strong> that can take us from <code>i</code> to <code>j</code>.</p>

<p>Return <code>true</code><em> if it is possible to traverse between all such pairs of indices,</em><em> or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -&gt; 2 -&gt; 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 &gt; 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 &gt; 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 &gt; 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 &gt; 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,9,5]
<strong>Output:</strong> false
<strong>Explanation:</strong> No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,3,12,8]
<strong>Output:</strong> true
<strong>Explanation:</strong> There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='greatest-common-divisor-traversal'
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if self.rank[pu] < self.rank[v]:
            pu, pv = pv, pu

        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N = len(nums)
        uf = DSU(N)
        factors = defaultdict(list)

        for i, x in enumerate(nums):
            for factor in range(2, int(math.sqrt(x)) + 1):
                if x % factor == 0:
                    factors[factor].append(i)

                    while x % factor == 0:
                        x //= factor
                
            if x > 1:
                factors[x].append(i)
        
        for A in factors.values():
            for a, b in zip(A, A[1:]):
                uf.union(a, b)
        
        p = uf.find(0)
        for i in range(N):
            if uf.find(i) != p: return False
        
        return True
```
