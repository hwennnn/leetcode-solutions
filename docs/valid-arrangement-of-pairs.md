---
id: valid-arrangement-of-pairs
title: Valid Arrangement of Pairs
description: Problem Description and Solution for Valid Arrangement of Pairs
sidebar_label: 2097. Valid Arrangement of Pairs
sidebar_position: 2097
---

# [2097. Valid Arrangement of Pairs](https://leetcode.com/problems/valid-arrangement-of-pairs/)

```py title=valid-arrangement-of-pairs.py
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        din, dout = Counter(), Counter()
        
        for x, y in pairs:
            graph[x].append(y)
            dout[x] += 1
            din[y] += 1
        
        head = pairs[0][0]
        for x in dout:
            if dout[x] - din[x] == 1:
                head = x
                break
        
        stack = [head]
        routes = []
        
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            routes.append(stack.pop())
        
        routes.reverse()
        
        return [[routes[i], routes[i + 1]] for i in range(len(routes) - 1)]
```


