---
id: number-of-visible-people-in-a-queue
title: Number of Visible People in a Queue
description: Problem Description and Solution for Number of Visible People in a Queue
sidebar_label: 1944. Number of Visible People in a Queue
sidebar_position: 1944
---

# [1944. Number of Visible People in a Queue](https://leetcode.com/problems/number-of-visible-people-in-a-queue/)

```py title=number-of-visible-people-in-a-queue.py
class Solution:
    def canSeePersonsCount(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        stack = []
        
        for i, v in enumerate(A):
            while stack and A[stack[-1]] <= v:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            stack.append(i)
            
        return res
```


