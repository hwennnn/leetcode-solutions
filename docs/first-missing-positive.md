---
id: first-missing-positive
title: First Missing Positive
description: Problem Description and Solution for First Missing Positive
sidebar_label: 41. First Missing Positive
sidebar_position: 41
---

# [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

```py title=first-missing-positive.py
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        for i in range(n):
            while (nums[i] > 0 and nums[i] <= n) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i+1:
                return i + 1
        
        return n + 1
```

```cpp title=first-missing-positive.cpp
class Solution{
public:
    int firstMissingPositive(vector<int>& A)
    {
        int n = A.size();
        for(int i = 0; i < n; ++ i)
            while(A[i] > 0 && A[i] <= n && A[A[i] - 1] != A[i])
                swap(A[i], A[A[i] - 1]);
        
        for(int i = 0; i < n; ++ i)
            if(A[i] != i + 1)
                return i + 1;
        
        return n + 1;
    }
};
```


