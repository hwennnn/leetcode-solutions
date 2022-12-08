---
id: implement-rand10-using-rand7
title: Implement Rand10() Using Rand7()
description: Problem Description and Solution for Implement Rand10() Using Rand7()
sidebar_label: 470. Implement Rand10() Using Rand7()
sidebar_position: 470
---

# [470. Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)

```py title=implement-rand10-using-rand7.py
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        rand40 = 40
        
        while rand40 >= 40:
            rand40 = (rand7() -1)*7 + rand7() - 1
        
        return rand40 % 10 + 1
        
```


