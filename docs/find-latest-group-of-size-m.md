---
id: find-latest-group-of-size-m
title: Find Latest Group of Size M
description: Problem Description and Solution for Find Latest Group of Size M
sidebar_label: 1562. Find Latest Group of Size M
sidebar_position: 1562
---

# [1562. Find Latest Group of Size M](https://leetcode.com/problems/find-latest-group-of-size-m/)

```py title=find-latest-group-of-size-m.py
class Solution:
    def findLatestStep(self, A: List[int], m: int) -> int:
        if m == len(A): return m
        
        length = [0] * (len(A) + 2)
        res = -1
        for i, a in enumerate(A):
            left, right = length[a - 1], length[a + 1]
        
            if left == m or right == m:
                res = i
            length[a - left] = length[a + right] = left + right + 1
        
        return res
```

```cpp title=find-latest-group-of-size-m.cpp
class Solution {
public:
     int findLatestStep(vector<int>& A, int m) {
        int res = -1, n = A.size();
        vector<int> length(n + 2), count(n + 1);
        for (int i = 0; i < n; ++i) {
            int a = A[i], left = length[a - 1], right = length[a + 1];
            length[a] = length[a - left] = length[a + right] = left + right + 1;
            count[left]--;
            count[right]--;
            count[length[a]]++;
            if (count[m])
                res = i + 1;
        }
        return res;
    }
};
```


