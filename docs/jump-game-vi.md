---
id: jump-game-vi
title: Jump Game VI
description: Problem Description and Solution for Jump Game VI
sidebar_label: 1696. Jump Game VI
sidebar_position: 1696
---

# [1696. Jump Game VI](https://leetcode.com/problems/jump-game-vi/)

```py title=jump-game-vi.py
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = collections.deque()
        
        for i in range(len(nums)):
            mmax = 0 if not queue else nums[queue[0]]
            nums[i] += mmax
            
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            
            if i - queue[0] >= k:
                queue.popleft()
        
        return nums[-1]
```


