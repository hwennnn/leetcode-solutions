---
id: maximum-candies-you-can-get-from-boxes
title: Maximum Candies You Can Get from Boxes
description: Problem Description and Solution for Maximum Candies You Can Get from Boxes
sidebar_label: 1298. Maximum Candies You Can Get from Boxes
sidebar_position: 1298
---

# [1298. Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/)

```py title=maximum-candies-you-can-get-from-boxes.py
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
        boxes = set(initialBoxes)
        bfs = [i for i in boxes if status[i]]
        
        for i in bfs:
            for b in containedBoxes[i]:
                boxes.add(b)
                if status[b]: bfs.append(b)
            
            for k in keys[i]:
                if status[k] == 0 and k in boxes:
                    bfs.append(k)
                
                status[k] = 1
        
        return sum([candies[v] for v in bfs])
                    
```


