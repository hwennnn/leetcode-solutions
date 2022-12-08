---
id: maximum-number-of-events-that-can-be-attended
title: Maximum Number of Events That Can Be Attended
description: Problem Description and Solution for Maximum Number of Events That Can Be Attended
sidebar_label: 1353. Maximum Number of Events That Can Be Attended
sidebar_position: 1353
---

# [1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

```cpp title=maximum-number-of-events-that-can-be-attended.cpp
class Solution {
public:
    int maxEvents(vector<vector<int>>& A) {
        priority_queue <int,vector<int>,greater<int>> pq;
        sort(A.begin(), A.end());
        int i = 0, res = 0, n = A.size();
        for (int d = 1; d <= 100000; d++){
            while (pq.size() && pq.top() < d)
                pq.pop();
                
            while (i < n && A[i][0] == d)
                pq.push(A[i++][1]);
            
            if (pq.size()){
                pq.pop();
                ++res;
            }
        }
        
        return res;
    }
};
```


