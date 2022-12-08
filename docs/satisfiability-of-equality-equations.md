---
id: satisfiability-of-equality-equations
title: Satisfiability of Equality Equations
description: Problem Description and Solution for Satisfiability of Equality Equations
sidebar_label: 990. Satisfiability of Equality Equations
sidebar_position: 990
---

# [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/)

```py title=satisfiability-of-equality-equations.py
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
    def equationsPossible(self, equations: List[str]) -> bool:
        N = len(equations)
        uf = UnionFind()

        for x, e, _ , y in equations:
            if e == "=":
                uf.union(x, y)
        
        return not any(e == "!" and uf.find(x) == uf.find(y) for x, e, _, y in equations)

```


