---
id: advantage-shuffle
title: Advantage Shuffle
description: Problem Description and Solution for Advantage Shuffle
sidebar_label: 870. Advantage Shuffle
sidebar_position: 870
---

# [870. Advantage Shuffle](https://leetcode.com/problems/advantage-shuffle/)

```py title=advantage-shuffle.py
class Solution:
    def advantageCount(self, A, B):
        A = sorted(A)
        take = collections.defaultdict(list)
        
        for b in sorted(B)[::-1]:
            if b < A[-1]: 
                take[b].append(A.pop())
                
        return [(take[b] or A).pop() for b in B]
        
```


