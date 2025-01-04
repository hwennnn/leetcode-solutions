---
title: Disjoint Set (Union Find)
tags:
  - data-structures
  - union-find
  - graph
date: 2025-01-05
---

## Introduction

A **disjoint set** is a data structure that keeps track of a partition of a set into disjoint (non-overlapping) subsets. A union-find algorithm is an algorithm that performs two useful operations on such a partition:

- Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
- Union: Join two subsets into a single subset.

## Implementation

### Array Implementation with `N` elements

```py
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if (pu == pv): return

        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu

        # ensure self.rank[pu] >= self.rank[pv]
        self.parent[pv] = pu
        if self.rank[pu] == self.rank[pv]:
            self.rank[pu] += 1
```

### Map Implementation

```py
class DSU:
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
```

## Path Compression

**Path compression** is a critical optimization technique used in the `find()` operation of **Union Find** data structure. It helps achieve near-constant time complexity for operations by flattening the tree structure during `find()` operations.

### How Path Compression Works

When we perform a `find()` operation to locate the root of an element, instead of just returning the root, path compression makes all traversed nodes point directly to the root. This optimization ensures that subsequent `find()` operations on these nodes will be much faster.

For example, consider this initial chain of nodes:

```bash
1 -> 2 -> 3 -> 4 -> 5
```

After performing `find(1)` with path compression, the structure becomes:

```bash
1 -> 5
2 -> 5
3 -> 5
4 -> 5
5
```

This flattening of the tree structure means that future `find()` operations on any of these nodes will take just one step to reach the root.

With path compression, the amortized time complexity of operations becomes $O(α(n))$, where $α$ is the inverse Ackermann function. This function grows so slowly that for all practical purposes, we can consider the operations to be effectively constant time.

## Union by Rank

**Union by rank** is another important optimization technique used alongside path compression. While path compression optimizes the `find()` operation, union by rank optimizes the `union()` operation by keeping the tree balanced.

### How Rank Works

The rank of a node represents the height of the tree rooted at that node. When performing a union operation:

1. We compare the ranks of the two roots
2. The root with the smaller rank is attached to the root with the larger rank
3. If the ranks are equal, we attach either root to the other and increment the resulting root's rank by 1

For example, consider two trees:

```bash
Tree 1 (rank 1):    Tree 2 (rank 1):
     3                   7
    /                   /
   1                   6
```

After `union(3, 7)` with equal ranks, one tree is attached to the other and the rank is incremented:

```bash
     3 (rank 2)
    /  \
   1    7
        /
       6
```

### Benefits of Union by Rank

1. Prevents the creation of long chains of nodes
2. Ensures that trees remain relatively balanced
3. Guarantees a logarithmic height bound of $O(\log n)$
4. When combined with path compression, helps achieve the near-constant amortized time complexity of $O(α(n))$

## References

- [Union-Find Algorithm](https://jojozhuang.github.io/algorithm/algorithm-union-find/)
