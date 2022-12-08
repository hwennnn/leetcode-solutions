---
id: top-k-frequent-elements
title: Top K Frequent Elements
description: Problem Description and Solution for Top K Frequent Elements
sidebar_label: 347. Top K Frequent Elements
sidebar_position: 347
---

# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

```py title=top-k-frequent-elements.py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        
        c = collections.Counter(nums).items()

        for num,freq in c:
            buckets[freq].append(num)
            
        res = []
        pointer = len(buckets) - 1
        
        while k > 0 and pointer >= 0:
            while k > 0 and len(buckets[pointer]) > 0:
                res.append(buckets[pointer].pop())
                k -= 1
            pointer -= 1
            
        return res
```

```cpp title=top-k-frequent-elements.cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        
        for (int num: nums)
            ++mp[num];
        
        
        vector<vector<int>> buckets(nums.size() + 1); 
        for (auto v: mp)
            buckets[v.second].push_back(v.first);
        
        
        vector<int> res;
        for (int i = buckets.size() - 1; i >= 0 && res.size() < k; --i){
            for (int num : buckets[i]){
                res.push_back(num);
                
                if (res.size() == k)
                    break;
            }
        }
        
        return res;
    }
};
```


