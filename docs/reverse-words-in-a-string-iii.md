---
id: reverse-words-in-a-string-iii
title: Reverse Words in a String III
description: Problem Description and Solution for Reverse Words in a String III
sidebar_label: 557. Reverse Words in a String III
sidebar_position: 557
---

# [557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

```py title=reverse-words-in-a-string-iii.py
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(x[::-1] for x in s.split())
```


