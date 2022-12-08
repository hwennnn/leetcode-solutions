---
id: remove-boxes
title: Remove Boxes
description: Problem Description and Solution for Remove Boxes
sidebar_label: 546. Remove Boxes
sidebar_position: 546
---

# [546. Remove Boxes](https://leetcode.com/problems/remove-boxes/)

```py title=remove-boxes.py
import functools
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        def dfs(i,j,k):
            if i>j: return 0
            cnt=0
            while (i+cnt)<=j and boxes[i]==boxes[i+cnt]:
                cnt+=1
            i2=i+cnt
            res=dfs(i2,j,0)+(k+cnt)**2
            for m in range(i2,j+1):
                if boxes[m]==boxes[i]:
                    res=max(res, dfs(i2,m-1,0)+dfs(m,j,k+cnt))
            return res
        return dfs(0,len(boxes)-1,0)
```


