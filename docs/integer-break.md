---
id: integer-break
title: Integer Break
description: Problem Description and Solution for Integer Break
sidebar_label: 343. Integer Break
sidebar_position: 343
---

# [343. Integer Break](https://leetcode.com/problems/integer-break/)

```py title=integer-break.py
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        
        m = 1
        while n > 4:
            m *= 3
            n -= 3
        
        m *= n
        
        return m
```

```cpp title=integer-break.cpp
class Solution {
public:
    int integerBreak(int n) {
        if(n==2)    return 1;
        if(n==3)    return 2;
        
        int res = 1;
        
        while (n > 4){
            res *= 3;
            n -= 3;
        }
            
        res *= n;
        
        return res;
    }
};
```


