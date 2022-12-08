---
id: largest-component-size-by-common-factor
title: Largest Component Size by Common Factor
description: Problem Description and Solution for Largest Component Size by Common Factor
sidebar_label: 952. Largest Component Size by Common Factor
sidebar_position: 952
---

# [952. Largest Component Size by Common Factor](https://leetcode.com/problems/largest-component-size-by-common-factor/)

```py title=largest-component-size-by-common-factor.py
class DSU:
    def __init__(self, n):
        self.graph = list(range(n))

    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])

        return self.graph[x]

    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        self.graph[ux] = uy

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        dsu = DSU(n)
        primes = defaultdict(list)
        
        def getPrimesSet(x):
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    return getPrimesSet(x // i) | set([i])
            
            return set([x])
        
        for i, x in enumerate(nums):
            p = getPrimesSet(x)
            for prime in p:
                primes[prime].append(i)
        
        for indexes in primes.values():
            for x, y in zip(indexes, indexes[1:]):
                dsu.union(x, y)
        
        return max(Counter(dsu.find(i) for i in range(n)).values())
            
```


