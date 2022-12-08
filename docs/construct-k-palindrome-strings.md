---
id: construct-k-palindrome-strings
title: Construct K Palindrome Strings
description: Problem Description and Solution for Construct K Palindrome Strings
sidebar_label: 1400. Construct K Palindrome Strings
sidebar_position: 1400
---

# [1400. Construct K Palindrome Strings](https://leetcode.com/problems/construct-k-palindrome-strings/)

```py title=construct-k-palindrome-strings.py
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(i & 1 for i in collections.Counter(s).values()) <= k <= len(s)

```


