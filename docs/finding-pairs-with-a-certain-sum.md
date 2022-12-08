---
id: finding-pairs-with-a-certain-sum
title: Finding Pairs With a Certain Sum
description: Problem Description and Solution for Finding Pairs With a Certain Sum
sidebar_label: 1865. Finding Pairs With a Certain Sum
sidebar_position: 1865
---

# [1865. Finding Pairs With a Certain Sum](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/)

```py title=finding-pairs-with-a-certain-sum.py
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.mp1 = collections.Counter(nums1)
        self.mp2 = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.mp2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.mp2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        
        for k,v in self.mp1.items():
            if tot - k in self.mp2:
                count += v * self.mp2[tot - k]
        
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
```


