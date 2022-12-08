---
id: sort-array-by-parity
title: Sort Array By Parity
description: Problem Description and Solution for Sort Array By Parity
sidebar_label: 905. Sort Array By Parity
sidebar_position: 905
---

# [905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)

```py title=sort-array-by-parity.py
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        
        for j, x in enumerate(nums):
            if x % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
        return nums
        
```

```cpp title=sort-array-by-parity.cpp
class Solution {
public:
    vector<int> sortArrayByParity(vector<int> &A) {
        for (int i = 0, j = 0; j < A.size(); j++)
            if (A[j] % 2 == 0) swap(A[i++], A[j]);
        return A;
    }
};
```


