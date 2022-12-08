---
id: delete-and-earn
title: Delete and Earn
description: Problem Description and Solution for Delete and Earn
sidebar_label: 740. Delete and Earn
sidebar_position: 740
---

# [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/)

```py title=delete-and-earn.py
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        buckets = [0] * 10001
        
        for x in nums:
            buckets[x] += x
        
        dp = [0] * 10001
        dp[0] = buckets[0]
        dp[1] = buckets[1]
        
        for i in range(2, 10001):
            dp[i] = max(dp[i - 1], dp[i - 2] + buckets[i])

        return dp[-1]
```

```cpp title=delete-and-earn.cpp
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<int> buckets(10001,0);
        
        for (int i = 0; i < nums.size(); i++){
            buckets[nums[i]] += nums[i];
        }
        
        vector<int> dp(10001,0);
        dp[0] = buckets[0];
        dp[1] = buckets[1];
        
        for (int i = 2; i < buckets.size(); i++){
            dp[i] = max(dp[i-1], buckets[i]+dp[i-2]);
        }
        
        return dp[10000];
    }
};
```


