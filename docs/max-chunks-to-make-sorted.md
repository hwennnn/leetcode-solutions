---
id: max-chunks-to-make-sorted
title: Max Chunks To Make Sorted
description: Problem Description and Solution for Max Chunks To Make Sorted
sidebar_label: 769. Max Chunks To Make Sorted
sidebar_position: 769
---

# [769. Max Chunks To Make Sorted](https://leetcode.com/problems/max-chunks-to-make-sorted/)

```cpp title=max-chunks-to-make-sorted.cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        int right = -1, res = 0;
        
        for (int i = 0; i < arr.size(); i++){
            right = max(right, arr[i]);
            res += right == i;
        }
        
        return res;
    }
};
```


