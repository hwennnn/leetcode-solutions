---
title: 40. Combination Sum II
draft: false
tags: 
  - leetcode-medium
  - array
  - backtracking
date: 2024-08-13
---

[Problem Link](https://leetcode.com/problems/combination-sum-ii/)

## Description

---
<p>Given a collection of candidate numbers (<code>candidates</code>) and a target number (<code>target</code>), find all unique combinations in <code>candidates</code>&nbsp;where the candidate numbers sum to <code>target</code>.</p>

<p>Each number in <code>candidates</code>&nbsp;may only be used <strong>once</strong> in the combination.</p>

<p><strong>Note:</strong>&nbsp;The solution set must not contain duplicate combinations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> candidates = [10,1,2,7,6,1,5], target = 8
<strong>Output:</strong> 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> candidates = [2,5,2,1,2], target = 5
<strong>Output:</strong> 
[
[1,2,2],
[5]
]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;candidates.length &lt;= 100</code></li>
	<li><code>1 &lt;=&nbsp;candidates[i] &lt;= 50</code></li>
	<li><code>1 &lt;= target &lt;= 30</code></li>
</ul>


## Solution

---
### Python3
``` py title='combination-sum-ii'
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        res = []

        def go(index, curr, path):
            if curr == target:
                res.append(path[:])
                return
            
            if index == N: return

            for i in range(index, N):
                if i > index and candidates[i] == candidates[i - 1]: continue

                if candidates[i] + curr <= target:
                    path.append(candidates[i])
                    go(i + 1, candidates[i] + curr, path)
                    path.pop()

        go(0, 0, [])
        return res

```

