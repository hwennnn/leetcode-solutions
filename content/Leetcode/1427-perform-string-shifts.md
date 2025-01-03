---
title: 1427. Perform String Shifts
draft: false
tags: 
  - array
  - math
  - string
date: 2020-04-14
---

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-blue.svg)

## Description

---
null

## Solution

---
### Python
``` py title='perform-string-shifts'
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
             
        l = len(s)
        count = 0

        for pair in shift:
            if pair[0] == 0:
                count += pair[1]
            else:
                count -= pair[1]

        if count == 0: return s

        if count < 0:
            n = l - (abs(count)%l)
            s = s[n:] + s[:n]

        else:
            count = count%l
            s = s[count:] + s[:count]

        return s


            
            

```

