---
id: remove-element
title: Remove Element
description: Problem Description and Solution for Remove Element
sidebar_label: 27. Remove Element
sidebar_position: 27
---

# [27. Remove Element](https://leetcode.com/problems/remove-element/)

```py title=remove-element.py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        
        return count
```


