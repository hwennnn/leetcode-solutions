---
id: most-common-word
title: Most Common Word
description: Problem Description and Solution for Most Common Word
sidebar_label: 819. Most Common Word
sidebar_position: 819
---

# [819. Most Common Word](https://leetcode.com/problems/most-common-word/)

```py title=most-common-word.py
class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        ban = set(banned)
        words = re.findall(r'\w+', p.lower())
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]
```


