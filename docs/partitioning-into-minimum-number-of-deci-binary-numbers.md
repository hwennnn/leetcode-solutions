---
id: partitioning-into-minimum-number-of-deci-binary-numbers
title: Partitioning Into Minimum Number Of Deci-Binary Numbers
description: Problem Description and Solution for Partitioning Into Minimum Number Of Deci-Binary Numbers
sidebar_label: 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
sidebar_position: 1689
---

# [1689. Partitioning Into Minimum Number Of Deci-Binary Numbers](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/)

```py title=partitioning-into-minimum-number-of-deci-binary-numbers.py
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(x) for x in n)
```


