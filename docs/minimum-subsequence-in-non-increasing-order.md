---
id: minimum-subsequence-in-non-increasing-order
title: Minimum Subsequence in Non-Increasing Order
description: Problem Description and Solution for Minimum Subsequence in Non-Increasing Order
sidebar_label: 1403. Minimum Subsequence in Non-Increasing Order
sidebar_position: 1403
---

# [1403. Minimum Subsequence in Non-Increasing Order](https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/)

```py title=minimum-subsequence-in-non-increasing-order.py
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        while sum(res) <= sum(nums):
            res.append(nums.pop())
        
        return res
    
```

```cpp title=minimum-subsequence-in-non-increasing-order.cpp
class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        vector<int> res;
        auto sub_sum = 0, half_sum = accumulate(begin(nums), end(nums), 0) / 2;
        priority_queue<int> pq(begin(nums), end(nums));
        while (sub_sum <= half_sum) {
            res.push_back(pq.top());
            sub_sum += res.back();
            pq.pop();
        }
        return res;
    }
};
```


