---
id: h-index
title: H-Index
description: Problem Description and Solution for H-Index
sidebar_label: 274. H-Index
sidebar_position: 274
---

# [274. H-Index](https://leetcode.com/problems/h-index/)

```cpp title=h-index.cpp
class Solution {
public:
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int n=citations.size();
        for(int i=0;i<n;i++){
            if(citations[i]>=n-i){
                return n-i;
            }
        }
        return 0;
    }
};
```


