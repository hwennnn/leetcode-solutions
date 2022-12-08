---
id: partition-equal-subset-sum
title: Partition Equal Subset Sum
description: Problem Description and Solution for Partition Equal Subset Sum
sidebar_label: 416. Partition Equal Subset Sum
sidebar_position: 416
---

# [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

```py title=partition-equal-subset-sum.py
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        target = total // 2
        if total & 1: return False
        
        bits = 1
        
        for x in nums:
            bits |= (bits << x)
        
        return (bits & (1 << target)) > 0
```

```cpp title=partition-equal-subset-sum.cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        bitset<10001> bits(1);
        int total = 0;
        
        for (auto n:nums)
            bits |= bits << n, total += n;
        
        return !(total&1) && bits[total / 2];
    }
};
```


