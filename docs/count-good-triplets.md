---
id: count-good-triplets
title: Count Good Triplets
description: Problem Description and Solution for Count Good Triplets
sidebar_label: 1534. Count Good Triplets
sidebar_position: 1534
---

# [1534. Count Good Triplets](https://leetcode.com/problems/count-good-triplets/)

```py title=count-good-triplets.py
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i]-arr[j]) <= a and abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        res += 1
        
        return res
```

```cpp title=count-good-triplets.cpp
class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int n = arr.size();
        int ans = 0;
        for (int i=0; i < n; ++i){
            for (int j = i+1; j < n; ++j){
                for (int k=j+1; k<n; ++k){
                    ans += abs(arr[i]-arr[j])<=a && abs(arr[j]-arr[k])<=b && abs(arr[i]-arr[k])<=c;
                }
            }
        }
        
        return ans;
    }
};
```


