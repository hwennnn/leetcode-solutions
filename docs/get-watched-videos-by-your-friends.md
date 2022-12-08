---
id: get-watched-videos-by-your-friends
title: Get Watched Videos by Your Friends
description: Problem Description and Solution for Get Watched Videos by Your Friends
sidebar_label: 1311. Get Watched Videos by Your Friends
sidebar_position: 1311
---

# [1311. Get Watched Videos by Your Friends](https://leetcode.com/problems/get-watched-videos-by-your-friends/)

```py title=get-watched-videos-by-your-friends.py
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], uid: int, level: int) -> List[str]:
        
        visited = {uid}
        deq = collections.deque([(uid, 0)])
        res = set()
        
        while deq:
            node, l = deq.popleft()
            
            if l > level: break
            
            if l == level: res.add(node)
            
            for nei in friends[node]:
                if nei not in visited:
                    deq.append((nei, l + 1))
                    visited.add(nei)
            
        videos = Counter([v for i in res for v in watchedVideos[i]])
        
        return sorted(videos, key = lambda x: (videos[x], x))
                
```


