---
id: groups-of-strings
title: Groups of Strings
description: Problem Description and Solution for Groups of Strings
sidebar_label: 2157. Groups of Strings
sidebar_position: 2157
---

# [2157. Groups of Strings](https://leetcode.com/problems/groups-of-strings/)

```py title=groups-of-strings.py
class UnionFind:
    def __init__(self):
        self._parent = {}
        self._size = {}
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self._size[a] < self._size[b]:
            a, b = b, a
        self._parent[b] = a
        self._size[a] += self._size[b]
    
    def find(self, x):
        if x not in self._parent:
            self._parent[x] = x
            self._size[x] = 1
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x
        
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        
        def getMask(word):
            mask = 0
            
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))
            
            return mask
        
        uf = UnionFind()
        
        for word in words:
            mask = getMask(word)
            
            for i in range(26):
                if mask & (1 << i):
                    uf.union(mask, mask ^ (1 << i))
        
        count = Counter()
        
        for word in words:
            count[uf.find(getMask(word))] += 1
        
        return [len(count), max(count.values())]
        
```


