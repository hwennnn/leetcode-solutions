---
id: remove-all-occurrences-of-a-substring
title: Remove All Occurrences of a Substring
description: Problem Description and Solution for Remove All Occurrences of a Substring
sidebar_label: 1910. Remove All Occurrences of a Substring
sidebar_position: 1910
---

# [1910. Remove All Occurrences of a Substring](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/)

```py title=remove-all-occurrences-of-a-substring.py
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        queue = collections.deque()
        pn = len(part)
        
        def check():
            i = -1
            for _ in range(pn):
                if queue[i] != part[i]: return False
                i -= 1
            
            return True
        
        for x in s:
            queue.append(x)
            
            while len(queue) >= pn and check():
                for _ in range(pn):
                    queue.pop()
            
        return "".join(queue)
```


