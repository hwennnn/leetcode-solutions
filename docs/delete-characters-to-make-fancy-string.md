---
id: delete-characters-to-make-fancy-string
title: Delete Characters to Make Fancy String
description: Problem Description and Solution for Delete Characters to Make Fancy String
sidebar_label: 1957. Delete Characters to Make Fancy String
sidebar_position: 1957
---

# [1957. Delete Characters to Make Fancy String](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)

```py title=delete-characters-to-make-fancy-string.py
class Solution:
    def makeFancyString(self, s: str) -> str:
        deque = collections.deque()
        
        for c in s:
            deque.append(c)
            
            while len(deque) >= 3 and deque[-1] == deque[-2] == deque[-3]:
                deque.pop()
        
        return "".join(deque)
```


