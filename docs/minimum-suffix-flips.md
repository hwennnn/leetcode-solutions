---
id: minimum-suffix-flips
title: Minimum Suffix Flips
description: Problem Description and Solution for Minimum Suffix Flips
sidebar_label: 1529. Minimum Suffix Flips
sidebar_position: 1529
---

# [1529. Minimum Suffix Flips](https://leetcode.com/problems/minimum-suffix-flips/)

```cpp title=minimum-suffix-flips.cpp
class Solution {
public:
    int minFlips(string target) {
        int n = target.size();
        int flips = 0;
        char status = '0';
        
        for (int i = 0; i < n; i++){
            
            if (target[i] != status){
                flips++;
                
                status = status == '0' ? '1' : '0';
            }
                
        }
        
        return flips;
            
           
    }
};
```


