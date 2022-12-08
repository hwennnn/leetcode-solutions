---
id: di-string-match
title: DI String Match
description: Problem Description and Solution for DI String Match
sidebar_label: 942. DI String Match
sidebar_position: 942
---

# [942. DI String Match](https://leetcode.com/problems/di-string-match/)

```py title=di-string-match.py
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        n = len(s)
        queue = deque([x for x in range(n + 1)])
        
        for x in s:
            if x == "I":
                res.append(queue.popleft())
            else:
                res.append(queue.pop())
        
        res.append(queue.pop())
        
        return res
```


