---
title: 213. House Robber II
draft: false
tags: 
  - leetcode-medium
  - array
  - dynamic-programming
date: 2020-08-15
---

[Problem Link](https://leetcode.com/problems/house-robber-ii/)

## Description

---
<p>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are <strong>arranged in a circle.</strong> That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and&nbsp;<b>it will automatically contact the police if two adjacent houses were broken into on the same night</b>.</p>

<p>Given an integer array <code>nums</code> representing the amount of money of each house, return <em>the maximum amount of money you can rob tonight <strong>without alerting the police</strong></em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## Solution

---
### Python3
``` py title='house-robber-ii'
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        def rob_helper(start, end):
            rob = not_rob = 0
            
            for i in range(start, end):
                rob, not_rob = not_rob + nums[i], max(not_rob, rob)
            
            return max(rob, not_rob)
        
        return max(rob_helper(0, len(nums) - 1), rob_helper(1, len(nums)))
```
### C++
``` cpp title='house-robber-ii'
class Solution {
public:
    int rob1(vector<int>& nums){
        int n = nums.size();
        
        int rob = 0, not_rob = 0;
        for (int i = 0; i < n-1; i++){
            int yes = not_rob + nums[i];
            int no = max(rob, not_rob);
            
            rob = yes;
            not_rob = no;
        }
        
        return max(rob, not_rob);
    }
    
    int rob2(vector<int>& nums){
        int n = nums.size();
        
        int rob = 0, not_rob = 0;
        for (int i = 1; i < n; i++){
            int yes = not_rob + nums[i];
            int no = max(rob, not_rob);
            
            rob = yes;
            not_rob = no;
        }
        
        return max(rob, not_rob);
    }
    
    int rob(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        return max(rob1(nums), rob2(nums));
    }
};
```

