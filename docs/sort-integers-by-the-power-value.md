---
id: sort-integers-by-the-power-value
title: Sort Integers by The Power Value
description: Problem Description and Solution for Sort Integers by The Power Value
sidebar_label: 1387. Sort Integers by The Power Value
sidebar_position: 1387
---

# [1387. Sort Integers by The Power Value](https://leetcode.com/problems/sort-integers-by-the-power-value/)

```py title=sort-integers-by-the-power-value.py
class Solution:
    def getKth(self, lo, hi, k):
        cache = {1: 1}
        def fn(n):
            if n not in cache:
                if n % 2 == 0:
                    cache[n] = 1 + fn(n / 2)
                else:
                    cache[n] = 1 + fn(3*n + 1)
            return cache[n]
        res = sorted((fn(i), i) for i in range(lo, hi+1))
        print(cache)
        return res[k-1][1]
```

```cpp title=sort-integers-by-the-power-value.cpp
class Solution {
    #define ar array
public:
    int getKth(int lo, int hi, int k) {
        vector<ar<int,2>> mp;
        
        for (int i = lo; i <= hi; i++){
            mp.push_back({0,i});
            int j = i;
            while (j > 1){
                if (j&1)
                    j = 3 * j + 1;
                else
                    j = j / 2;
                ++mp.back()[0];
            }
        }
        
        sort(mp.begin(), mp.end());
        
        return mp[k-1][1];
    }
};
```


