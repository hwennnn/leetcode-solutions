---
id: most-visited-sector-in-a-circular-track
title: Most Visited Sector in  a Circular Track
description: Problem Description and Solution for Most Visited Sector in  a Circular Track
sidebar_label: 1560. Most Visited Sector in  a Circular Track
sidebar_position: 1560
---

# [1560. Most Visited Sector in  a Circular Track](https://leetcode.com/problems/most-visited-sector-in-a-circular-track/)

```py title=most-visited-sector-in-a-circular-track.py
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        dic = {rounds[0]:1}
        N = len(rounds)
        for i in range(N-1):
            this_round = rounds[i]
            next_round = rounds[i+1]

            while this_round != next_round:
                if this_round < n:
                    this_round += 1
                else:
                    this_round = 1

                if this_round not in dic:
                    dic[this_round] = 1
                else:
                    dic[this_round] += 1

        m = max(dic.values())
        res = []
        for key in dic:
            if dic[key] == m:
                res.append(key)
        res.sort()
        return res
            

            
            
```

```cpp title=most-visited-sector-in-a-circular-track.cpp
class Solution {
public:
    vector<int> mostVisited(int n, vector<int>& A) {
        vector<int> res;
        for (int i = A[0]; i <= A[A.size() - 1]; ++i)
            res.push_back(i);
        if (res.size() > 0) return res;
        for (int i = 1; i <= A[A.size() - 1]; ++i)
            res.push_back(i);
        for (int i = A[0]; i <= n; ++i)
            res.push_back(i);
        return res;
    }
};
```


