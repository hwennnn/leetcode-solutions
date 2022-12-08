---
id: shuffle-an-array
title: Shuffle an Array
description: Problem Description and Solution for Shuffle an Array
sidebar_label: 384. Shuffle an Array
sidebar_position: 384
---

# [384. Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/)

```py title=shuffle-an-array.py
from random import randint

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.nums[:]
        
        for i in range(self.n):
            index = randint(i, self.n - 1)
            res[i], res[index] = res[index], res[i]
        
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```


