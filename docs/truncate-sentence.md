---
id: truncate-sentence
title: Truncate Sentence
description: Problem Description and Solution for Truncate Sentence
sidebar_label: 1816. Truncate Sentence
sidebar_position: 1816
---

# [1816. Truncate Sentence](https://leetcode.com/problems/truncate-sentence/)

```py title=truncate-sentence.py
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
```


