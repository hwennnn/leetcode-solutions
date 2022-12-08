---
id: people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
title: People Whose List of Favorite Companies Is Not a Subset of Another List
description: Problem Description and Solution for People Whose List of Favorite Companies Is Not a Subset of Another List
sidebar_label: 1452. People Whose List of Favorite Companies Is Not a Subset of Another List
sidebar_position: 1452
---

# [1452. People Whose List of Favorite Companies Is Not a Subset of Another List](https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/)

```py title=people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list.py
class Solution:
    def peopleIndexes(self, fc: List[List[str]]) -> List[int]:
        ans = []
        
        s = [set(cs) for cs in fc]
        
        res = []
        
        for i,s1 in enumerate(s):
            
            if all(i == j or not s1.issubset(s2) for j,s2 in enumerate(s)):
                res.append(i)
        
        return res
```


