---
id: shuffle-string
title: Shuffle String
description: Problem Description and Solution for Shuffle String
sidebar_label: 1528. Shuffle String
sidebar_position: 1528
---

# [1528. Shuffle String](https://leetcode.com/problems/shuffle-string/)

```py title=shuffle-string.py
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [None] * len(s)
        
        for idx,x in enumerate(indices):
            res[x] = s[idx]
        
        return "".join(res)
            
```

```cpp title=shuffle-string.cpp
class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        
        for (int i = 0; i < indices.size(); i++){
            
            while (indices[i] != i){
                swap(s[i], s[indices[i]]);
                swap(indices[i],indices[indices[i]]);
            }
        }
        
        return s;
    }
};
```


