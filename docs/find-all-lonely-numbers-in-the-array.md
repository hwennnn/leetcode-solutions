---
id: find-all-lonely-numbers-in-the-array
title: Find All Lonely Numbers in the Array
description: Problem Description and Solution for Find All Lonely Numbers in the Array
sidebar_label: 2150. Find All Lonely Numbers in the Array
sidebar_position: 2150
---

# [2150. Find All Lonely Numbers in the Array](https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/)

```py title=find-all-lonely-numbers-in-the-array.py
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        
        for x in counter.keys():
            if counter[x] == 1 and x - 1 not in counter and x + 1 not in counter:
                res.append(x)
        
        return res
```


