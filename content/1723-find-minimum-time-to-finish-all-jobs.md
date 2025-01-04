---
title: 1723. Find Minimum Time to Finish All Jobs
draft: false
tags: 
  - leetcode-hard
  - array
  - dynamic-programming
  - backtracking
  - bit-manipulation
  - bitmask
date: 2022-06-12
---

[Problem Link](https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/)

## Description

---
<p>You are given an integer array <code>jobs</code>, where <code>jobs[i]</code> is the amount of time it takes to complete the <code>i<sup>th</sup></code> job.</p>

<p>There are <code>k</code> workers that you can assign jobs to. Each job should be assigned to <strong>exactly</strong> one worker. The <strong>working time</strong> of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the <strong>maximum working time</strong> of any worker is <strong>minimized</strong>.</p>

<p><em>Return the <strong>minimum</strong> possible <strong>maximum working time</strong> of any assignment. </em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> jobs = [3,2,3], k = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> By assigning each person one job, the maximum time is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> jobs = [1,2,4,7,8], k = 2
<strong>Output:</strong> 11
<strong>Explanation:</strong> Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= jobs.length &lt;= 12</code></li>
	<li><code>1 &lt;= jobs[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## Solution

---
### Python
``` py title='find-minimum-time-to-finish-all-jobs'
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        res = float('inf')
        A = [0] * k
        
        def go(index):
            nonlocal res, A
            
            if index == n:
                res = min(res, max(A))
                return
            
            seen = set()
            
            for j in range(k):
                if A[j] in seen: continue
                if A[j] + jobs[index] >= res: continue
                
                seen.add(A[j])
                A[j] += jobs[index]
                go(index + 1)
                A[j] -= jobs[index]
        
        go(0)
        
        return res
```
