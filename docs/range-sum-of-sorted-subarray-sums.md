---
id: range-sum-of-sorted-subarray-sums
title: Range Sum of Sorted Subarray Sums
description: Problem Description and Solution for Range Sum of Sorted Subarray Sums
sidebar_label: 1508. Range Sum of Sorted Subarray Sums
sidebar_position: 1508
---

# [1508. Range Sum of Sorted Subarray Sums](https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/)

```py title=range-sum-of-sorted-subarray-sums.py
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        arr = []
        M = int(1e9+7)
        
        for i in range(n):
            s = nums[i]
            for j in range(i+1,n):
                s += nums[j]
                nums.append(s)
        
        nums = sorted(nums)
        res = 0
        for i in range(left-1, right):
            res = (res + nums[i])%M
        
        return res%M
```

```cpp title=range-sum-of-sorted-subarray-sums.cpp
class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {
        vector<int> v;
        
        for (int i = 0; i < n; ++i){
            int s = 0;
            for (int j = i; j < n; ++j){
                s += nums[j];
                v.push_back(s);
                
            }
        }
        
        sort(v.begin(),v.end());
        
        --left, --right;
        
        int ans = 0, M = 1e9+7;
        for (int i = left; i <= right; ++i){
            ans = (ans+v[i])%M;
        }
        
        return ans;
        
    }
};
```


