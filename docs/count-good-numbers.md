---
id: count-good-numbers
title: Count Good Numbers
description: Problem Description and Solution for Count Good Numbers
sidebar_label: 1922. Count Good Numbers
sidebar_position: 1922
---

# [1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers/)

```py title=count-good-numbers.py
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        M = 10 ** 9 + 7
        even = (n + 1) // 2
        odd = n // 2
        
        def ipower(base, exp):
            if exp == 0: return 1
            
            ans = ipower(base, exp // 2)
            
            if exp % 2 == 0:
                return (ans * ans) % M
            else:
                return (base * ans * ans) % M
            
        return (ipower(5, even) * ipower(4, odd)) % M
        
        
```

```cpp title=count-good-numbers.cpp
class Solution {
public:
    int M = 1e9 + 7;
    
    long long power(long long base, long long exp){
        if (exp == 0) return 1;
        
        long long res = power(base, exp / 2) % M;
        
        res *= res;
        res %= M;
        
        if (exp & 1)
            res *= base;
        res %= M;
        
        return res;
    }
    int countGoodNumbers(long long n) {
        long long even = (n + 1) / 2;
        long long odd = n - even;
        
        return (power(5, even) * power(4, odd)) % M;
    }
};
```


