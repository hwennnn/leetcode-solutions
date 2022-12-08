---
id: prime-arrangements
title: Prime Arrangements
description: Problem Description and Solution for Prime Arrangements
sidebar_label: 1175. Prime Arrangements
sidebar_position: 1175
---

# [1175. Prime Arrangements](https://leetcode.com/problems/prime-arrangements/)

```py title=prime-arrangements.py
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = [True] * (n + 1)
        
        for prime in range(2, int(math.sqrt(n)) + 1):
            if primes[prime]:
                for composite in range(prime * prime, n + 1, prime):
                    primes[composite] = False
                    
        cnt = sum(primes[2:])

        return math.factorial(cnt) * math.factorial(n - cnt) % (10**9 + 7)
        
```


