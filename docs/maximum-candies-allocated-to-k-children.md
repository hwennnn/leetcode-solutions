---
id: maximum-candies-allocated-to-k-children
title: Maximum Candies Allocated to K Children
description: Problem Description and Solution for Maximum Candies Allocated to K Children
sidebar_label: 2226. Maximum Candies Allocated to K Children
sidebar_position: 2226
---

# [2226. Maximum Candies Allocated to K Children](https://leetcode.com/problems/maximum-candies-allocated-to-k-children/)

```py title=maximum-candies-allocated-to-k-children.py
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        total = sum(candies)
        
        if total < k: return 0
        
        def good(b):
            count = 0
            
            for x in candies:
                count += x // b
            
            return count >= k

        left, right = 1, 10 ** 18

        while left < right:
            mid = left + (right - left + 1) // 2

            if good(mid):
                left = mid
            else:
                right = mid - 1
        # print(left, right)
        return left
            
            
```


