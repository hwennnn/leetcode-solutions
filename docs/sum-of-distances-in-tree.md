---
id: sum-of-distances-in-tree
title: Sum of Distances in Tree
description: Problem Description and Solution for Sum of Distances in Tree
sidebar_label: 834. Sum of Distances in Tree
sidebar_position: 834
---

# [834. Sum of Distances in Tree](https://leetcode.com/problems/sum-of-distances-in-tree/)

```py title=sum-of-distances-in-tree.py
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res
```


