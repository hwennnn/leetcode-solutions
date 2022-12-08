---
id: maximize-the-confusion-of-an-exam
title: Maximize the Confusion of an Exam
description: Problem Description and Solution for Maximize the Confusion of an Exam
sidebar_label: 2024. Maximize the Confusion of an Exam
sidebar_position: 2024
---

# [2024. Maximize the Confusion of an Exam](https://leetcode.com/problems/maximize-the-confusion-of-an-exam/)

```py title=maximize-the-confusion-of-an-exam.py
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def go(key):
            left = res = count = 0
            
            for right, x in enumerate(answerKey):
                if x == key:
                    count += 1
                
                while count > k:
                    if answerKey[left] == key:
                        count -= 1
                    left += 1
                
                res = max(res, right - left + 1)
            
            return res
        
        return max(go('T'), go('F'))
```


