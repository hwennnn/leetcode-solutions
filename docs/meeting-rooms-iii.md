---
id: meeting-rooms-iii
title: Meeting Rooms III
description: Problem Description and Solution for Meeting Rooms III
sidebar_label: 2402. Meeting Rooms III
sidebar_position: 2402
---

# [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/)

```py title=meeting-rooms-iii.py
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        usedCount = [0] * n
        
        availableRooms = list(range(n))
        usedRooms = []
        
        for start, end in meetings:
            while usedRooms and usedRooms[0][0] <= start:
                t, roomId = heappop(usedRooms)
                heappush(availableRooms, roomId)
            
            if availableRooms:
                r = heappop(availableRooms)
                heappush(usedRooms, (end, r))
            else:
                endTime, r = heappop(usedRooms)
                heappush(usedRooms, (endTime + end - start, r))
                
            usedCount[r] += 1
            
        return usedCount.index(max(usedCount))
```


