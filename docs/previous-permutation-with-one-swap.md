---
id: previous-permutation-with-one-swap
title: Previous Permutation With One Swap
description: Problem Description and Solution for Previous Permutation With One Swap
sidebar_label: 1053. Previous Permutation With One Swap
sidebar_position: 1053
---

# [1053. Previous Permutation With One Swap](https://leetcode.com/problems/previous-permutation-with-one-swap/)

```py title=previous-permutation-with-one-swap.py
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        if n <= 1: return arr
        
        index = -1
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                index = i - 1
                break
                
        if index == -1: return arr
        for i in range(n - 1, index - 1, -1):
            if arr[i] < arr[index] and arr[i] != arr[i - 1]:
                arr[i], arr[index] = arr[index], arr[i]
                break
        
        return arr
        
```


