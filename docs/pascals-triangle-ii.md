---
id: pascals-triangle-ii
title: Pascal's Triangle II
description: Problem Description and Solution for Pascal's Triangle II
sidebar_label: 119. Pascal's Triangle II
sidebar_position: 119
---

# [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/)

```py title=pascals-triangle-ii.py
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t = [[1], [1, 1]]
        
        for index in range(2, rowIndex + 1):
            tt = t[-1]
            tmp = [1] + [0] * (index - 1) + [1]
            for i in range(1, len(tmp) - 1):
                left = tt[i - 1]
                right = tt[-1] if i + 1 >= len(tt) else tt[i]
                tmp[i] = left + right
            
            t.append(tmp)
        
        return t[rowIndex]
```

```cpp title=pascals-triangle-ii.cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        int n = rowIndex+1;
        vector<int> tri(n,0);
        tri[0] = 1;
        
        
        for (int i = 1; i < n; i++){
             for (int j = i; j > 0; j--){
                 tri[j] += tri[j-1];
             }
        }
           
                
        
        return tri;
        
    }
};
```


