---
id: number-of-students-unable-to-eat-lunch
title: Number of Students Unable to Eat Lunch
description: Problem Description and Solution for Number of Students Unable to Eat Lunch
sidebar_label: 1700. Number of Students Unable to Eat Lunch
sidebar_position: 1700
---

# [1700. Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)

```py title=number-of-students-unable-to-eat-lunch.py
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = collections.deque(students)
        
        for s in sandwiches:
            if s in queue:
                while queue[0] != s:
                    queue.append(queue.popleft())
                
                queue.popleft()
            
            else:
                return len(queue)
        
        return 0
```


