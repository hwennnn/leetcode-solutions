---
id: robot-return-to-origin
title: Robot Return to Origin
description: Problem Description and Solution for Robot Return to Origin
sidebar_label: 657. Robot Return to Origin
sidebar_position: 657
---

# [657. Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/)

```py title=robot-return-to-origin.py
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        x = y = 0
        
        for i in moves:
            
            if (i == "U"): y+=1 
                
            elif (i == "D"): y-=1
            
            elif(i == "R"): x+=1
            
            elif(i == "L"): x-=1
            
        
        return True if (x==0 and y==0) else False
```


