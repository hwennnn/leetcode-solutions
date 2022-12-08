---
id: process-tasks-using-servers
title: Process Tasks Using Servers
description: Problem Description and Solution for Process Tasks Using Servers
sidebar_label: 1882. Process Tasks Using Servers
sidebar_position: 1882
---

# [1882. Process Tasks Using Servers](https://leetcode.com/problems/process-tasks-using-servers/)

```py title=process-tasks-using-servers.py
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(x, i) for i,x in enumerate(servers)]
        heapq.heapify(available)
        running, res = [], []
        j = t = 0
        n = len(tasks)
        
        while j < n:
            while running and running[0][0] <= t:
                _, capacity, index = heapq.heappop(running)
                heapq.heappush(available, (capacity, index))
            
            while available and j < n and t >= j:
                capacity, index = heapq.heappop(available)
                heapq.heappush(running, (t + tasks[j], capacity, index))
                res.append(index)
                j += 1
            
            t = t + 1 if available else running[0][0]
        
        return res
```


