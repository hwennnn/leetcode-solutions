---
id: reverse-words-in-a-string
title: Reverse Words in a String
description: Problem Description and Solution for Reverse Words in a String
sidebar_label: 151. Reverse Words in a String
sidebar_position: 151
---

# [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

```py title=reverse-words-in-a-string.py
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        curr = ""

        for x in s + " ":
            if x == " ":
                if curr:
                    res.append(curr)
                    curr = ""
            else:
                curr += x

        return " ".join(res[::-1])
```


