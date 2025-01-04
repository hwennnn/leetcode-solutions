---
title: Segment Tree
tags:
  - data-structures
  - range-queries
  - tree
date: 2023-10-30
---

## Introduction

A **segment tree** is a data structure that supports two operations: processing a complex range query and updating an array value in $O(\lg n)$ time. Unlike [[Binary Indexed Tree]] which only supports sum queries, a **Segment Tree** supports other complex queries such as min/max queries. However, segment tree is usually harder to implement and requires more memory.

### Structure of the Segment Tree

A segment tree is a binary tree such that the nodes on the bottom level of the tree correspond to the array elements, and the other nodes contain its child information for processing range queries.

We compute and store the sum of the elements of the whole array, i.e. the sum of the segment  $a[0 \dots n-1]$ . We then split the array into two halves  $a[0 \dots n/2-1]$  and  $a[n/2 \dots n-1]$  and compute the sum of each halve and store them. Each of these two halves in turn are split in half, and so on until all segments reach size  $1$.

### Why the size of the array is $4n$?

The segment tree is stored as an array of $4n$ elements where n is the size of original array and a power of two. The first level of the tree contains a single node (the root), the second level will contain two vertices, in the third it will contain four vertices, until the number of vertices reaches  $n$ .

Thus the number of vertices in the worst case can be estimated by the sum  $1 + 2 + 4 + \dots + 2^{\lceil\log_2 n\rceil} \lt 2^{\lceil\log_2 n\rceil + 1} \lt 4n$ .

The height of the Segment Tree is  $O(\log n)$ , because when going down from the root to the leaves the size of the segments decreases approximately by half.

## Implementation

### Standard Segment Tree

```py
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, arr)

    def build(self, v, tl, tr, arr):
        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = tl + (tr - tl) // 2
            self.build(v * 2, tl, tm, arr)
            self.build(v * 2 + 1, tm + 1, tr, arr)
            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]

    def query(self, v, tl, tr, l, r):
        if l > r: return 0

        if tl == l and tr == r:
            return self.tree[v]
        else:
            tm = tl + (tr - tl) // 2

        return self.query(v * 2, tl, tm, l, min(tm, r)) + self.query(v * 2 + 1, tm + 1, tr, max(tm + 1, l), r)

    def update(self, v, tl, tr, pos, value):
        if tl == tr:
            self.tree[v] = value
        else:
            tm = tl + (tr - tl) // 2

            if pos <= tm:
                self.update(v * 2, tl, tm, pos, value)
            else:
                self.update(v * 2 + 1, tm + 1, tr, pos, value)

            self.tree[v] = self.tree[v * 2] + self.tree[v * 2 + 1]
```

### Lazy Propagation

```py
class LazySegmentTree:
    def __init__(self, N):
        self.n = N
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)

    def build(self, v, tl, tr, arr):
        if tl > tr: return

        if tl == tr:
            self.tree[v] = arr[tl]
        else:
            tm = tl + (tr - tl) // 2
            self.build(v * 2, tl, tm, arr)
            self.build(v * 2 + 1, tm + 1, tr, arr)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])

    def push(self, v):
        self.tree[v*2] += self.lazy[v]
        self.lazy[v*2] += self.lazy[v]
        self.tree[v*2+1] += self.lazy[v]
        self.lazy[v*2+1] += self.lazy[v]
        self.lazy[v] = 0

    def query(self, v, tl, tr, l, r):
        if l > r: return -inf

        if tl >= l and tr <= r:
            return self.tree[v]

        self.push(v)
        tm = tl + (tr - tl) // 2

        return max(self.query(2 * v, tl, tm, l, min(tm, r)), self.query(2 * v + 1, tm + 1, tr, max(tm + 1, l), r))

    def update(self, v, tl, tr, l, r, value):
        if l > r: return

        if tl >= l and tr <= r:
            self.tree[v] += value
            self.lazy[v] += value
        else:
            self.push(v)

            tm = tl + (tr - tl) // 2

            self.update(2 * v, tl, tm, l, min(tm, r), value)
            self.update(2 * v + 1, tm + 1, tr, max(tm + 1, l), r, value)
            self.tree[v] = max(self.tree[2 * v], self.tree[2 * v + 1])

```

### C++

```cpp
void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = max(t[v*2], t[v*2 + 1]);
    }
}

void push(int v) {
    t[v*2] += lazy[v];
    lazy[v*2] += lazy[v];
    t[v*2+1] += lazy[v];
    lazy[v*2+1] += lazy[v];
    lazy[v] = 0;
}

void update(int v, int tl, int tr, int l, int r, int addend) {
    if (l > r)
        return;
    if (l == tl && tr == r) {
        t[v] += addend;
        lazy[v] += addend;
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), addend);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, addend);
        t[v] = max(t[v*2], t[v*2+1]);
    }
}

int query(int v, int tl, int tr, int l, int r) {
    if (l > r)
        return -INF;
    if (l == tl && tr == r)
        return t[v];
    push(v);
    int tm = (tl + tr) / 2;
    return max(query(v*2, tl, tm, l, min(r, tm)),
               query(v*2+1, tm+1, tr, max(l, tm+1), r));
}
```

## Complexity

- Time complexity: $O(\lg n)$ for query and update operations
- Space complexity: $O(4n)$, where n is the size of the original array

## Resources

1. [Why the array size is 4n](https://www.quora.com/Why-does-4-%2A-N-space-have-to-be-allocated-for-a-segment-tree-where-N-is-the-size-of-the-original-array/answer/Manohar-Reddy-Poreddy?ch=15&oid=57482364&share=02b1dda6&srid=hmOb7S&target_type=answer)
2. [Lazy Propagation](https://www.topcoder.com/thrive/articles/range-operations-lazy-propagation)
3. [Block Placement Queries - Leetcode](https://leetcode.com/problems/block-placement-queries/)
