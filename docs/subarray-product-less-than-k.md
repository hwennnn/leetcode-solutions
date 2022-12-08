---
id: subarray-product-less-than-k
title: Subarray Product Less Than K
description: Problem Description and Solution for Subarray Product Less Than K
sidebar_label: 713. Subarray Product Less Than K
sidebar_position: 713
---

# [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)

```py title=subarray-product-less-than-k.py
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        left = right = 0
        curr = 1
        
        while right < n:
            curr *= nums[right]
            
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            
            res += right - left + 1
            right += 1
        
        return res
```

```cpp title=subarray-product-less-than-k.cpp
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int c = 1, res = 0;
        
        for (int i = 0,j = 0; j < nums.size(); j++){
            c *= nums[j];
            while (i <= j && c >= k)
                c /= nums[i++];
            res += (j - i + 1);
        }
        
        return res;
    }
};
```


