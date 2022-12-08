---
id: maximum-score-from-removing-stones
title: Maximum Score From Removing Stones
description: Problem Description and Solution for Maximum Score From Removing Stones
sidebar_label: 1753. Maximum Score From Removing Stones
sidebar_position: 1753
---

# [1753. Maximum Score From Removing Stones](https://leetcode.com/problems/maximum-score-from-removing-stones/)

```py title=maximum-score-from-removing-stones.py
from heapq import heappush, heappop, heapify

class Solution:
    # heap
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return min((a+b+c)//2 , a+b+c - max(a,b,c))
        res = 0
        stones = [-a,-b,-c]
        heapify(stones)
        
        while abs(stones[0]) > 0 and abs(stones[1]) > 0:
            first = heappop(stones) + 1
            second = heappop(stones) + 1
            
            heappush(stones, first)
            heappush(stones, second)
            
            res += 1
            
        return res
            
            
```

```cpp title=maximum-score-from-removing-stones.cpp
class Solution {
public:
    int maximumScore(int a, int b, int c) {
        if (a < b)
            return maximumScore(b, a, c);
        
        if (b < c)
            return maximumScore(a, c, b);
        
        return b == 0 ? 0 : 1 + maximumScore(a-1, b-1, c);
    }
};
```


