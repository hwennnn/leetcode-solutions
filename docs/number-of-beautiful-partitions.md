---
id: number-of-beautiful-partitions
title: Number of Beautiful Partitions
description: Problem Description and Solution for Number of Beautiful Partitions
sidebar_label: 2478. Number of Beautiful Partitions
sidebar_position: 2478
---

# [2478. Number of Beautiful Partitions](https://leetcode.com/problems/number-of-beautiful-partitions/)

```py title=number-of-beautiful-partitions.py
class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        N = len(s)
        M = 10 ** 9 + 7
        
        primes = set(["2", "3", "5", "7"])
        
        if s[0] not in primes or s[-1] in primes: return 0
        
        @cache
        def go(index, parts):
            if parts == 0 and index <= N: return 1
            if index >= N: return 0
            
            res = go(index + 1, parts)
            
            if s[index] in primes and s[index - 1] not in primes:
                res += go(index + minLength, parts - 1)
            
            return res % M
        
        return go(minLength, k - 1)
```

```cpp title=number-of-beautiful-partitions.cpp
class Solution {
public:
    const int M = 1e9 + 7;
    int cache[1001][1001];

    bool isPrime(char x) {
        return x == '2' || x == '3' || x == '5' || x == '7';
    }

    int go(int index, int parts, string& s, int k, int minLength, int N) {
        if (cache[index][parts] != -1) return cache[index][parts];
            
        if (parts >= k) return cache[index][parts] = 0;

        if (parts == k - 1) return cache[index][parts] = (N - index >= minLength);

        int res = 0;

        for (int j = index + minLength; j < N - (k - parts - 1) * minLength + 1; j++) {
            if (isPrime(s[j]) && !isPrime(s[j - 1])) {
                res += go(j, parts + 1, s, k, minLength, N);
                res %= M;
            }
        }

        return cache[index][parts] = res;
    }

    int beautifulPartitions(string s, int k, int minLength) {
        int N = s.size();
        memset(cache, -1, sizeof(cache));

        if (!isPrime(s[0]) || isPrime(s[N - 1])) return 0;
        
        return go(0, 0, s, k, minLength, N);
    }
};
```


