---
title: 1426. Counting Elements
draft: false
tags: 
  - leetcode-easy
  - array
  - hash-table
date: 2020-04-07
---

[Problem Link](https://leetcode.com/problems/counting-elements/)

## Description

---
null

## Solution

---
### Python3
``` py title='counting-elements'
class Solution:
    def countElements(self, nums: List[int]) -> int:
        c = set(nums)

        return sum([1 for x in nums if x+1 in nums])
```

