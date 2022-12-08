---
id: average-salary-excluding-the-minimum-and-maximum-salary
title: Average Salary Excluding the Minimum and Maximum Salary
description: Problem Description and Solution for Average Salary Excluding the Minimum and Maximum Salary
sidebar_label: 1491. Average Salary Excluding the Minimum and Maximum Salary
sidebar_position: 1491
---

# [1491. Average Salary Excluding the Minimum and Maximum Salary](https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/)

```py title=average-salary-excluding-the-minimum-and-maximum-salary.py
class Solution:
    def average(self, salary: List[int]) -> float:
        mmax, mmin = max(salary), min(salary)
        res = count = 0
        
        for x in salary:
            if x != mmax and x != mmin:
                res += x
                count += 1
        
        return res / count
```


