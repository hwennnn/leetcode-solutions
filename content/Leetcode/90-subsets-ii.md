---
title: 90. Subsets II
draft: false
tags: 
  - leetcode-medium
  - array
  - backtracking
  - bit-manipulation
date: 2019-10-09
---

[Problem Link](https://leetcode.com/problems/subsets-ii/)

## Description

---
<p>Given an integer array <code>nums</code> that may contain duplicates, return <em>all possible</em> <span data-keyword="subset"><em>subsets</em></span><em> (the power set)</em>.</p>

<p>The solution set <strong>must not</strong> contain duplicate subsets. Return the solution in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2]
<strong>Output:</strong> [[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> [[],[0]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>


## Solution

---
### Python
``` py title='subsets-ii'
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        ans = [[]]
        start = 1
        
        for i in range(n):
            temp = []
            for j, num in enumerate(ans):
                if i > 0 and nums[i] == nums[i-1] and j < start: continue
                    
                c = num + [nums[i]]
                temp.append(c)
            
            start = len(ans)
            ans += temp
        
        return ans
                
        
```
### C++
``` cpp title='subsets-ii'
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            bool illegal = false;
            for (int j = 0; j < n; ++j)
                if (i >> j&1){
                    if (j > 0 && nums[j]==nums[j-1] && (i>>(j-1)&1) == 0){
                        illegal = true;
                        break;
                    }else{
                        c.push_back(nums[j]);
                    }
                }
                    
            if (!illegal){
                res.push_back(c);
            }
        }
        
        return res;
    }
};
```
### Python
``` py title='subsets-ii'
class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res

```

