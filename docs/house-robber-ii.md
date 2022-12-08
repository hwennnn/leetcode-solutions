---
id: house-robber-ii
title: House Robber II
description: Problem Description and Solution for House Robber II
sidebar_label: 213. House Robber II
sidebar_position: 213
---

# [213. House Robber II](https://leetcode.com/problems/house-robber-ii/)

```py title=house-robber-ii.py
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

```cpp title=house-robber-ii.cpp
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


