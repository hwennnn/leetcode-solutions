---
id: detect-pattern-of-length-m-repeated-k-or-more-times
title: Detect Pattern of Length M Repeated K or More Times
description: Problem Description and Solution for Detect Pattern of Length M Repeated K or More Times
sidebar_label: 1566. Detect Pattern of Length M Repeated K or More Times
sidebar_position: 1566
---

# [1566. Detect Pattern of Length M Repeated K or More Times](https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/)

```py title=detect-pattern-of-length-m-repeated-k-or-more-times.py
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        res = 0
        
        for i in range(n-m):
            
            if arr[i] != arr[i+m]:
                res = 0
                
            res += (arr[i] == arr[i+m])
            
            if res == (k-1)*m:
                return True
        
        return False
            
```

```cpp title=detect-pattern-of-length-m-repeated-k-or-more-times.cpp
class Solution {
public:
    bool containsPattern(vector<int>& arr, int m, int k) {
        int cnt=0;
        for(int i=0;i+m < arr.size(); i++){
            
            if(arr[i]!=arr[i+m]){
              cnt=0;  
            }
            cnt += (arr[i] == arr[i+m]);
            if(cnt == (k-1)*m)
                return true;
            
        }
        return false;
    }
};
```


