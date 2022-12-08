---
id: minimum-difference-between-largest-and-smallest-value-in-three-moves
title: Minimum Difference Between Largest and Smallest Value in Three Moves
description: Problem Description and Solution for Minimum Difference Between Largest and Smallest Value in Three Moves
sidebar_label: 1509. Minimum Difference Between Largest and Smallest Value in Three Moves
sidebar_position: 1509
---

# [1509. Minimum Difference Between Largest and Smallest Value in Three Moves](https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/)

```py title=minimum-difference-between-largest-and-smallest-value-in-three-moves.py
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 4: return 0
        nums = sorted(nums)
        res = float('inf')
        for i in range(4):
            res = min(res, nums[n-1-3+i] - nums[i])
        
        return res
```

```cpp title=minimum-difference-between-largest-and-smallest-value-in-three-moves.cpp
class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        if (n < 5) return 0;
        
        sort(nums.begin(), nums.end());
        
        return min({nums[n-4]-nums[0], nums[n-3]-nums[1], nums[n-2]-nums[2], nums[n-1]-nums[3]});
        
        
    }
};
```


