---
id: sliding-window-maximum
title: Sliding Window Maximum
description: Problem Description and Solution for Sliding Window Maximum
sidebar_label: 239. Sliding Window Maximum
sidebar_position: 239
---

# [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

```py title=sliding-window-maximum.py
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        queue = collections.deque()
        
        for i,x in enumerate(nums):
            while queue and x >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            
            if i + 1 >= k:
                res.append(nums[queue[0]])
                
            if queue and i + 1 - k >= queue[0]:
                queue.popleft()
        
        return res
```

```cpp title=sliding-window-maximum.cpp
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> deq;
        vector<int> res;
        
        for (int i = 0; i < nums.size(); i++){
            if (i >= k && deq.front() == nums[i-k])
                deq.pop_front();
            
            while (deq.size() > 0 && deq.back() < nums[i])
                deq.pop_back();
            
            deq.push_back(nums[i]);
            
            if (i >= k-1)
                res.push_back(deq.front());
            
        }
        
        return res;
    }
};
```


