---
id: partition-labels
title: Partition Labels
description: Problem Description and Solution for Partition Labels
sidebar_label: 763. Partition Labels
sidebar_position: 763
---

# [763. Partition Labels](https://leetcode.com/problems/partition-labels/)

```py title=partition-labels.py
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        indices = {x: i for i, x in enumerate(s)}
        i = 0
        curr = set()
        res = []
        s += "!"
        
        for j, x in enumerate(s):
            if j == n or (j != 0 and len(curr) == 0):
                res.append(j - i)
                i = j
                
                if j == n: break
            
            curr.add(x)
            
            if indices[x] == j:
                curr.remove(x)
        
        
        return res
                
```

```cpp title=partition-labels.cpp
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> res, pos(26, 0);  
        for (auto i = 0; i < S.size(); ++i){
          pos[S[i] - 'a'] = i;
        }
        
        int maxIdx = INT_MIN, lastIdx = 0;
        
        for (auto i = 0; i < S.size(); i++){
            maxIdx = max(maxIdx, pos[S[i] - 'a']);
            if (i == maxIdx){
                res.push_back(maxIdx - lastIdx + 1);
                lastIdx = i + 1;
            }
        }
        
        return res;      
    }
};
```


