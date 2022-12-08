---
id: minimum-length-of-string-after-deleting-similar-ends
title: Minimum Length of String After Deleting Similar Ends
description: Problem Description and Solution for Minimum Length of String After Deleting Similar Ends
sidebar_label: 1750. Minimum Length of String After Deleting Similar Ends
sidebar_position: 1750
---

# [1750. Minimum Length of String After Deleting Similar Ends](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/)

```py title=minimum-length-of-string-after-deleting-similar-ends.py
class Solution:
    def minimumLength(self, s: str) -> int:
        d = collections.deque(s)
        
        while len(d) >= 2 and d[0] == d[-1]:
            current = d[0]
            
            while len(d) > 0 and d[0] == current:
                d.popleft()
            
            while len(d) > 0 and d[-1] == current:
                d.pop()
        
        return len(d)
```


