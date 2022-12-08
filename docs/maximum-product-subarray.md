---
id: maximum-product-subarray
title: Maximum Product Subarray
description: Problem Description and Solution for Maximum Product Subarray
sidebar_label: 152. Maximum Product Subarray
sidebar_position: 152
---

# [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

```py title=maximum-product-subarray.py
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = pos = neg = nums[0]
        
        for x in nums[1:]:
            if x < 0:
                pos, neg = neg, pos
            
            pos = max(x, pos * x)
            neg = min(x, neg * x)
            
            res = max(res, pos)
        
        return res
```

```cpp title=maximum-product-subarray.cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int localMax = nums[0]; 
        int localMin = nums[0]; 
        int maxProd = nums[0]; 
        for(int i = 1; i < nums.size(); i ++){ 
            if(nums[i] > 0){ 
                localMax = max(localMax * nums[i], nums[i]); 
                localMin = min(localMin * nums[i], nums[i]); 
            } else{ 
                int localMaxNeg = max(localMin * nums[i], nums[i]); 
                localMin = min(localMax * nums[i], nums[i]); 
                localMax = localMaxNeg; 
            } 
            maxProd = max(maxProd, localMax); 
        } 
        return maxProd; 
    }
};
```


