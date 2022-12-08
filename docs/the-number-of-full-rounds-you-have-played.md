---
id: the-number-of-full-rounds-you-have-played
title: The Number of Full Rounds You Have Played
description: Problem Description and Solution for The Number of Full Rounds You Have Played
sidebar_label: 1904. The Number of Full Rounds You Have Played
sidebar_position: 1904
---

# [1904. The Number of Full Rounds You Have Played](https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/)

```py title=the-number-of-full-rounds-you-have-played.py
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        if finishTime < startTime:
            return self.numberOfRounds(startTime, '24:00') + self.numberOfRounds('00:00', finishTime)
        
        sHH, sMM = map(int, startTime.split(':'))
        fHH, fMM = map(int, finishTime.split(':'))
        
        start = sHH * 60 + sMM
        finish = fHH * 60 + fMM
        
        return max(0, finish // 15 - (start // 15 + (start % 15 > 0)))
```


