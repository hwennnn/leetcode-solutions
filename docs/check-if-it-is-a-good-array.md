---
id: check-if-it-is-a-good-array
title: Check If It Is a Good Array
description: Problem Description and Solution for Check If It Is a Good Array
sidebar_label: 1250. Check If It Is a Good Array
sidebar_position: 1250
---

# [1250. Check If It Is a Good Array](https://leetcode.com/problems/check-if-it-is-a-good-array/)

```cpp title=check-if-it-is-a-good-array.cpp
class Solution {
public:
    bool isGoodArray(vector<int>& A) {
        int res = A[0];
        for (int a: A)
            res = gcd(res, a);
        return res == 1;
    }
};
```


