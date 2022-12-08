---
id: count-primes
title: Count Primes
description: Problem Description and Solution for Count Primes
sidebar_label: 204. Count Primes
sidebar_position: 204
---

# [204. Count Primes](https://leetcode.com/problems/count-primes/)

```py title=count-primes.py
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1: return 0
        
        arr = [True] * n
        arr[0] = arr[1] = False
        
        for i in range(2, n):
            if arr[i]:
                for j in range(i * i, n, i):
                    arr[j] = False
        
        return sum(arr)
```

```cpp title=count-primes.cpp
class Solution {
public:
    int countPrimes(int n) {
        vector<bool> arr(n, false);
        int count = 0;
        
        if (n <=2){
            return 0;
        } 
        
       for (int i = 2; i < n; i++){
           if (!arr[i]){
               count++;
               
               for (int j = 2; i*j<=n; j++)
                   arr[i*j] = true;
           }
       }
        
        return count;
    }
};
```


