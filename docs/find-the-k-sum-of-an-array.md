---
id: find-the-k-sum-of-an-array
title: Find the K-Sum of an Array
description: Problem Description and Solution for Find the K-Sum of an Array
sidebar_label: 2386. Find the K-Sum of an Array
sidebar_position: 2386
---

# [2386. Find the K-Sum of an Array](https://leetcode.com/problems/find-the-k-sum-of-an-array/)

```py title=find-the-k-sum-of-an-array.py
class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        posSum = sum(x for x in nums if x > 0)
        A = sorted(abs(x) for x in nums)
        res = posSum
        maxHeap = [(-posSum + A[0], 0)]

        for _ in range(k - 1):
            nextSum, index = heappop(maxHeap)

            if index + 1 < N:
                # -(-nextSum - A[index + 1])
                heappush(maxHeap, (nextSum + A[index + 1], index + 1))
                # -(-nextSum + A[index] - A[index + 1])
                heappush(maxHeap, (nextSum - A[index] + A[index + 1], index + 1))
            
            res = -nextSum
        
        return res
```


