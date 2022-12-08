---
id: parallel-courses-ii
title: Parallel Courses II
description: Problem Description and Solution for Parallel Courses II
sidebar_label: 1494. Parallel Courses II
sidebar_position: 1494
---

# [1494. Parallel Courses II](https://leetcode.com/problems/parallel-courses-ii/)

```py title=parallel-courses-ii.py
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        pre = [0] * n
        paths = [n + 1] * (1 << n)
        target = (1 << n) - 1
        
        for x, y in relations:
            x -= 1
            y -= 1
            pre[y] |= (1 << x)
        
        queue = deque([(0, 0)])
        
        while queue:
            state, steps = queue.popleft()
            new_courses = []
            
            for i in range(n):
                if (state & pre[i]) != pre[i]: continue
                
                if state & (1 << i) > 0: continue
                
                new_courses.append(i)
            
            if len(new_courses) <= k:
                for course in new_courses:
                    state |= (1 << course)
                
                if state == target: return 1 + steps
                
                if steps + 1 < paths[state]:
                    queue.append((state, steps + 1))
                    paths[state] = steps + 1
            else:
                for comb in combinations(new_courses, k):
                    new_state = state
                    
                    for course in list(comb):
                        new_state |= (1 << course)
                    
                    if steps + 1 < paths[new_state]:
                        queue.append((new_state, steps + 1))
                        paths[new_state] = steps + 1
```

```cpp title=parallel-courses-ii.cpp
class Solution {
    int a[15],f[32768],o[32768];
public:
    int minNumberOfSemesters(int n, vector<vector<int>>& dependencies, int k) {
        memset(a,0,sizeof(a));
        int i,j,l;
        for(auto e:dependencies)a[e[1]-1]|=1<<e[0]-1;
        for(i=1;i<1<<n;i++)o[i]=o[i>>1]+(i&1);
        memset(f,127,sizeof(f));
        for(i=f[0]=0;i<1<<n;i++)if(f[i]<=n)
        {
            for(j=l=0;j<n;j++)if(!(i>>j&1)&&(a[j]&i)==a[j])l|=1<<j;
            for(j=l;j;j=j-1&l)if(o[j]<=k)f[i|j]=min(f[i|j],f[i]+1);
        }
        return f[(1<<n)-1];
    }
};
```


