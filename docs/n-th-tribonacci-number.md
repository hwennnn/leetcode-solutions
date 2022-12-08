---
id: n-th-tribonacci-number
title: N-th Tribonacci Number
description: Problem Description and Solution for N-th Tribonacci Number
sidebar_label: 1137. N-th Tribonacci Number
sidebar_position: 1137
---

# [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

```py title=n-th-tribonacci-number.py
class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
```

```cpp title=n-th-tribonacci-number.cpp
class Solution {
public:
    int arr[38];
    int recur(int n){
        if (arr[n] != -1) return arr[n];
        int result = recur(n-1) + recur(n-2) + recur(n-3);
        arr[n] = result;
        return result;
    }
    int tribonacci(int n) {
        fill_n(arr, 38, -1);
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 1;
        return recur(n);
    }
};
```


