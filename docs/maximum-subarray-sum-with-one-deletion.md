---
id: maximum-subarray-sum-with-one-deletion
title: Maximum Subarray Sum with One Deletion
description: Problem Description and Solution for Maximum Subarray Sum with One Deletion
sidebar_label: 1186. Maximum Subarray Sum with One Deletion
sidebar_position: 1186
---

# [1186. Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)

```py title=maximum-subarray-sum-with-one-deletion.py
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        
        dp1 = [arr[0] for _ in range(n)]
        dp2 = [arr[0] for _ in range(n)]
        
        for i in range(1, n):
            dp1[i] = max(dp1[i-1] + arr[i], arr[i])
            dp2[i] = max(dp2[i-1] + arr[i], arr[i])
            
            if i >= 2:
                dp1[i] = max(dp1[i], dp2[i - 2] + arr[i])
            
        return max(dp1)
```


