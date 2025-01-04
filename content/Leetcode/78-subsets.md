---
title: 78. Subsets
draft: false
tags: 
  - leetcode-medium
  - array
  - backtracking
  - bit-manipulation
date: 2020-10-03
---

[Problem Link](https://leetcode.com/problems/subsets/)

## Description

---
<p>Given an integer array <code>nums</code> of <strong>unique</strong> elements, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span> <em>(the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>All the numbers of&nbsp;<code>nums</code> are <strong>unique</strong>.</li>
</ul>


## Solution

---
### Python
``` py title='subsets'
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        for mask in range(1 << N):
            A = []

            for j in range(N):
                if mask & (1 << j):
                    A.append(nums[j])
            
            res.append(A)
        
        return res
```
### C++
``` cpp title='subsets'
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            for (int j = 0; j < n; ++j)
                if (i >> j&1)
                    c.push_back(nums[j]);
            res.push_back(c);
        }
        
        return res;
    }
};
```

