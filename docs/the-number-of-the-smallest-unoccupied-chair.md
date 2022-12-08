---
id: the-number-of-the-smallest-unoccupied-chair
title: The Number of the Smallest Unoccupied Chair
description: Problem Description and Solution for The Number of the Smallest Unoccupied Chair
sidebar_label: 1942. The Number of the Smallest Unoccupied Chair
sidebar_position: 1942
---

# [1942. The Number of the Smallest Unoccupied Chair](https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/)

```py title=the-number-of-the-smallest-unoccupied-chair.py
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        available = list(range(n))
        mp = collections.defaultdict(int)
        seats = []
        
        for i, (t1,t2) in enumerate(times):
            seats.append((t1, 1, i))
            seats.append((t2, 0, i))
        
        seats.sort()
        
        for time, isArrival, friend in seats:
            if isArrival:
                seat = heapq.heappop(available)
                if friend == targetFriend: return seat
                mp[friend] = seat
            else:
                seat = mp[friend]
                heapq.heappush(available, seat)
        
        return mp[targetFriend]
```


