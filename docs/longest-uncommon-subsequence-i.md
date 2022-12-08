---
id: longest-uncommon-subsequence-i
title: Longest Uncommon Subsequence I
description: Problem Description and Solution for Longest Uncommon Subsequence I
sidebar_label: 521. Longest Uncommon Subsequence I
sidebar_position: 521
---

# [521. Longest Uncommon Subsequence I](https://leetcode.com/problems/longest-uncommon-subsequence-i/)

```py title=longest-uncommon-subsequence-i.py
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
```


