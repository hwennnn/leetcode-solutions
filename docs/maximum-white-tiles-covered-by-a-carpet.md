---
id: maximum-white-tiles-covered-by-a-carpet
title: Maximum White Tiles Covered by a Carpet
description: Problem Description and Solution for Maximum White Tiles Covered by a Carpet
sidebar_label: 2271. Maximum White Tiles Covered by a Carpet
sidebar_position: 2271
---

# [2271. Maximum White Tiles Covered by a Carpet](https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/)

```py title=maximum-white-tiles-covered-by-a-carpet.py
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        prefix = [0]
        start = []
        tiles.sort()
        res = 0
        
        for x, y in tiles:
            prefix.append(prefix[-1] + y - x + 1)
            start.append(x)
        
        for i, (x, y) in enumerate(tiles):
            if y - x + 1 >= carpetLen:
                return carpetLen
            
            index = bisect_right(start, x + carpetLen) - 1
            x2, y2 = tiles[index]
            extra = 0
            
            if y2 - x + 1 >= carpetLen:
                extra = y2 - x + 1 - carpetLen
            
            
            total = prefix[index + 1] - prefix[i] - extra
            res = max(res, total)
        
        return res
        
        
        
```


