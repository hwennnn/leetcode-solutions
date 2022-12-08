---
id: most-popular-video-creator
title: Most Popular Video Creator
description: Problem Description and Solution for Most Popular Video Creator
sidebar_label: 2456. Most Popular Video Creator
sidebar_position: 2456
---

# [2456. Most Popular Video Creator](https://leetcode.com/problems/most-popular-video-creator/)

```py title=most-popular-video-creator.py
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        viewCount = defaultdict(int)
        popularVideo = {}
        mostViews = 0
        
        for creator, uid, view in zip(creators, ids, views):
            viewCount[creator] += view
            mostViews = max(mostViews, viewCount[creator])
            
            if creator not in popularVideo:
                popularVideo[creator] = (view, uid)
            else:
                if view > popularVideo[creator][0] or (view == popularVideo[creator][0] and uid < popularVideo[creator][1]):
                    popularVideo[creator] = (view, uid)
        
        res = []
        for creator, totalViews in viewCount.items():
            if totalViews == mostViews:
                res.append((creator, popularVideo[creator][1]))
        
        return res
                    
```


