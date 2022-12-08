---
id: subsets
title: Subsets
description: Problem Description and Solution for Subsets
sidebar_label: 78. Subsets
sidebar_position: 78
---

# [78. Subsets](https://leetcode.com/problems/subsets/)

```py title=subsets.py
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        n = len(nums)
        
        for mask in range(1 << n):
            h = 0
            curr = []
            
            for j in range(n):
                if mask & (1 << j) > 0:
                    curr.append(nums[j])
                    h |= (1 << j)
            
            if h not in seen:
                res.append(curr)
                seen.add(h)
        
        return res
```

```cpp title=subsets.cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            for (int j = 0; j < n; ++j)
                if (i >> j&1)
                    c.push_back(nums[j]);
            res.push_back(c);
        }
        
        return res;
    }
};
```


