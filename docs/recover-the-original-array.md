---
id: recover-the-original-array
title: Recover the Original Array
description: Problem Description and Solution for Recover the Original Array
sidebar_label: 2122. Recover the Original Array
sidebar_position: 2122
---

# [2122. Recover the Original Array](https://leetcode.com/problems/recover-the-original-array/)

```py title=recover-the-original-array.py
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        def good(k):
            cnt, res = Counter(nums), []
            
            for x in nums:
                if cnt[x] == 0: continue
                if cnt[x + k] == 0: return False, []
                
                cnt[x] -= 1
                cnt[x + k] -= 1
                res += [x + k // 2]
            
            return True, res
            
        
        for i in range(1, len(nums)):
            k = nums[i] - nums[0]
            
            if k > 0 and k % 2 == 0:
                valid, res = good(k)

                if valid:
                    return res
```


