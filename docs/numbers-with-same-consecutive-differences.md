---
id: numbers-with-same-consecutive-differences
title: Numbers With Same Consecutive Differences
description: Problem Description and Solution for Numbers With Same Consecutive Differences
sidebar_label: 967. Numbers With Same Consecutive Differences
sidebar_position: 967
---

# [967. Numbers With Same Consecutive Differences](https://leetcode.com/problems/numbers-with-same-consecutive-differences/)

```py title=numbers-with-same-consecutive-differences.py
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        
        def go(index, curr):
            if index == n:
                res.append(curr)
                return
            
            last = curr % 10
            
            for nxt in {last + k, last - k}:
                if 0 <= nxt < 10:
                    go(index + 1, curr * 10 + nxt)
        
        for x in range(1, 10):
            go(1, x)
        
        return res
```

```cpp title=numbers-with-same-consecutive-differences.cpp
class Solution {
public:
    vector<int> numsSameConsecDiff(int N, int K) {
        vector<int> cur = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
        for (int i = 2; i <= N; ++i) {
            vector<int> cur2;
            for (int x : cur) {
                int y = x % 10;
                if (x > 0 && y + K < 10)
                    cur2.push_back(x * 10 + y + K);
                if (x > 0 && K > 0 && y - K >= 0)
                    cur2.push_back(x * 10 + y - K);
            }
            cur = cur2;
        }
        return cur;
    }
};
```


