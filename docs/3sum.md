---
id: 3sum
title: 3Sum
description: Problem Description and Solution for 3Sum
sidebar_label: 15. 3Sum
sidebar_position: 15
---

# [15. 3Sum](https://leetcode.com/problems/3sum/)

```py title=3sum.py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3: return []
        
        nums.sort()
        res = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
                
            j, k = i + 1, n - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    
                    j += 1
                    k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1
        
        return res
```

```cpp title=3sum.cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        int n = nums.size();
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n-2; i++){
            
            if (i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            
            int l = i+1, r = n-1;
            
            while (l < r){
                int s = nums[i] + nums[l] + nums[r];
                
                if (s < 0)
                    l++;
                
                else if (s > 0)
                    r--;
                
                else{
                    vector<int> temp(3, 0);
                    temp[0] = nums[i];
                    temp[1] = nums[l];
                    temp[2] = nums[r];
                    res.push_back(temp);
                    
                    while (l < r && nums[l] == nums[l+1]) l++;
                    while (l < r && nums[r] == nums[r-1]) r--;
                    
                    l++;
                    r--;
                }
            }         
        }
        return res;
    }
};
```


