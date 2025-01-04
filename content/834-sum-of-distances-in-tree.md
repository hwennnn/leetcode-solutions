---
title: 834. Sum of Distances in Tree
draft: false
tags: 
  - leetcode-hard
  - dynamic-programming
  - tree
  - depth-first-search
  - graph
date: 2024-04-28
---

[Problem Link](https://leetcode.com/problems/sum-of-distances-in-tree/)

## Description

---
<p>There is an undirected connected tree with <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code> and <code>n - 1</code> edges.</p>

<p>You are given the integer <code>n</code> and the array <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.</p>

<p>Return an array <code>answer</code> of length <code>n</code> where <code>answer[i]</code> is the sum of the distances between the <code>i<sup>th</sup></code> node in the tree and all other nodes.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg" style="width: 304px; height: 224px;" />
<pre>
<strong>Input:</strong> n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
<strong>Output:</strong> [8,12,6,10,10,10]
<strong>Explanation:</strong> The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg" style="width: 64px; height: 65px;" />
<pre>
<strong>Input:</strong> n = 1, edges = []
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg" style="width: 144px; height: 145px;" />
<pre>
<strong>Input:</strong> n = 2, edges = [[1,0]]
<strong>Output:</strong> [1,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>The given input represents a valid tree.</li>
</ul>


## Solution

---
### Python
``` py title='sum-of-distances-in-tree'
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        count = [0] * n
        res = [0] * n

        def dfs(node, prev):
            for adj in graph[node]:
                if adj == prev: continue

                dfs(adj, node)
                count[node] += count[adj]
                res[node] += res[adj] + count[adj]
            
            count[node] += 1
        
        def dfs2(node, prev):
            for adj in graph[node]:
                if adj == prev: continue
                # closer -> count[adj] gets 1 closer to the root
                # further -> n - count[adj] gets 1 further to the root
                res[adj] = res[node] - count[adj] + n - count[adj]
                dfs2(adj, node)

        
        dfs(0, -1)
        dfs2(0, -1)

        return res
```
