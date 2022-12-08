---
id: k-similar-strings
title: K-Similar Strings
description: Problem Description and Solution for K-Similar Strings
sidebar_label: 854. K-Similar Strings
sidebar_position: 854
---

# [854. K-Similar Strings](https://leetcode.com/problems/k-similar-strings/)

```py title=k-similar-strings.py
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        N = len(s1)
        queue = deque([s1])
        level = 0
        visited = set([s1])

        while queue:
            n = len(queue)
            
            for _ in range(n):
                s = queue.popleft()
                
                if s == s2: return level
                
                s = list(s)
                
                i = 0
                while i < N and s[i] == s2[i]:
                    i += 1

                for j in range(i + 1, N):
                    if s[j] == s2[i]:
                        s[i], s[j] = s[j], s[i]
                        word = "".join(s)
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)
                        s[i], s[j] = s[j], s[i]
                
            level += 1
        
        return -1
```


