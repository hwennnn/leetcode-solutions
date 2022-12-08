---
id: rotate-array
title: Rotate Array
description: Problem Description and Solution for Rotate Array
sidebar_label: 189. Rotate Array
sidebar_position: 189
---

# [189. Rotate Array](https://leetcode.com/problems/rotate-array/)

```py title=rotate-array.py
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        def reverseL(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverseL(0, n - 1)
        reverseL(0, k - 1)
        reverseL(k, n - 1)
        
        
```

```cpp title=rotate-array.cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k %= n;
        
        reverse(nums.begin(), nums.end());
        reverse(nums.begin(), nums.begin()+k);
        reverse(nums.begin()+k, nums.end());
        
    }
};
```


