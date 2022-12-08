---
id: number-of-sub-arrays-with-odd-sum
title: Number of Sub-arrays With Odd Sum
description: Problem Description and Solution for Number of Sub-arrays With Odd Sum
sidebar_label: 1524. Number of Sub-arrays With Odd Sum
sidebar_position: 1524
---

# [1524. Number of Sub-arrays With Odd Sum](https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/)

```py title=number-of-sub-arrays-with-odd-sum.py
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        odd = even = res = 0
        M = 1000000007
        
        for num in arr:
            if num & 1:
                odd, even = even+1, odd
            else:
                odd, even = odd, even+1
                
            res += odd
        
        return res%M
        
```

```cpp title=number-of-sub-arrays-with-odd-sum.cpp
class Solution {
public:
    int numOfSubarrays(vector<int>& A) {
        int cur = 0, odd = 0, even = 1, mod = (int)1e9 + 7, res = 0;
        for (int a: A) {
            cur += a;
            if (cur%2){
                res = (res+even)%mod;
                odd++;
            }else{
                res = (res+odd)%mod;
                even++;
            }
        }
        return res;
    }
        
};
```


