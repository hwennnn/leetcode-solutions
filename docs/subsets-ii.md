---
id: subsets-ii
title: Subsets II
description: Problem Description and Solution for Subsets II
sidebar_label: 90. Subsets II
sidebar_position: 90
---

# [90. Subsets II](https://leetcode.com/problems/subsets-ii/)

```py title=subsets-ii.py
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        ans = [[]]
        start = 1
        
        for i in range(n):
            temp = []
            for j, num in enumerate(ans):
                if i > 0 and nums[i] == nums[i-1] and j < start: continue
                    
                c = num + [nums[i]]
                temp.append(c)
            
            start = len(ans)
            ans += temp
        
        return ans
                
        
```

```cpp title=subsets-ii.cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;
        
        for (int i=0; i < 1<<n; ++i){
            vector<int> c;
            bool illegal = false;
            for (int j = 0; j < n; ++j)
                if (i >> j&1){
                    if (j > 0 && nums[j]==nums[j-1] && (i>>(j-1)&1) == 0){
                        illegal = true;
                        break;
                    }else{
                        c.push_back(nums[j]);
                    }
                }
                    
            if (!illegal){
                res.push_back(c);
            }
        }
        
        return res;
    }
};
```


