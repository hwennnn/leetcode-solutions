---
id: greatest-sum-divisible-by-three
title: Greatest Sum Divisible by Three
description: Problem Description and Solution for Greatest Sum Divisible by Three
sidebar_label: 1262. Greatest Sum Divisible by Three
sidebar_position: 1262
---

# [1262. Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/)

```py title=greatest-sum-divisible-by-three.py
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0, 0, 0]
        
        for num in nums:
            
            for i in dp[:]:
                dp[(i+num)%3] = max(dp[(i+num)%3], num + i)
            
        
        return dp[0]
    
```

```cpp title=greatest-sum-divisible-by-three.cpp
class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        vector<int> dp {0,0,0}, dp2;
        
        for (int num : nums){
            dp2 = dp;
            
            for (int i : dp2){
                dp[(num+i)%3] = max(dp[(num+i)%3], num+i);
            }
        }
        
        return dp[0];
    }
};
```


