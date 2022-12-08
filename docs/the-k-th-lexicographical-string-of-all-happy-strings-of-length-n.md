---
id: the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
title: The k-th Lexicographical String of All Happy Strings of Length n
description: Problem Description and Solution for The k-th Lexicographical String of All Happy Strings of Length n
sidebar_label: 1415. The k-th Lexicographical String of All Happy Strings of Length n
sidebar_position: 1415
---

# [1415. The k-th Lexicographical String of All Happy Strings of Length n](https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

```py title=the-k-th-lexicographical-string-of-all-happy-strings-of-length-n.py
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        d = {"a":"bc", "b":"ac", "c":"ab"}
        q = collections.deque(["a","b","c"])
        
        while len(q[0]) < n:
            v = q.popleft()
            
            for u in d[v[-1]]:
                q.append(v+u)
        
        return q[k-1] if len(q) >= k else ""
```


