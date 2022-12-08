---
id: first-bad-version
title: First Bad Version
description: Problem Description and Solution for First Bad Version
sidebar_label: 278. First Bad Version
sidebar_position: 278
---

# [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

```py title=first-bad-version.py
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n
        
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
```


