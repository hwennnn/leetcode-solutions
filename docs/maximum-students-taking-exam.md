---
id: maximum-students-taking-exam
title: Maximum Students Taking Exam
description: Problem Description and Solution for Maximum Students Taking Exam
sidebar_label: 1349. Maximum Students Taking Exam
sidebar_position: 1349
---

# [1349. Maximum Students Taking Exam](https://leetcode.com/problems/maximum-students-taking-exam/)

```py title=maximum-students-taking-exam.py
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        rows, cols = len(seats), len(seats[0])
        A = []
        
        for row in seats:
            A.append(sum(1 << j for j in range(cols) if row[j] == "."))
        
        @cache
        def go(currRow, prev):
            if currRow == rows: return 0
            
            mask, res = A[currRow], 0
            
            for bits in range(1 << cols):
                if (bits & mask) == bits and (bits & (bits >> 1) == 0):
                    if (bits & (prev << 1) == 0) and (bits & (prev >> 1) == 0):
                        students = bin(bits).count("1")
                        res = max(res, students + go(currRow + 1, bits))
                
            return res
        
        return go(0, 0)
                
```


