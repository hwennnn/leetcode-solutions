---
id: count-common-words-with-one-occurrence
title: Count Common Words With One Occurrence
description: Problem Description and Solution for Count Common Words With One Occurrence
sidebar_label: 2085. Count Common Words With One Occurrence
sidebar_position: 2085
---

# [2085. Count Common Words With One Occurrence](https://leetcode.com/problems/count-common-words-with-one-occurrence/)

```py title=count-common-words-with-one-occurrence.py
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        res = 0
        
        for k in c1:
            if c1[k] == c2[k] == 1:
                res += 1
        
        return res
```


