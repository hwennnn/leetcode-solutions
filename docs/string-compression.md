---
id: string-compression
title: String Compression
description: Problem Description and Solution for String Compression
sidebar_label: 443. String Compression
sidebar_position: 443
---

# [443. String Compression](https://leetcode.com/problems/string-compression/)

```py title=string-compression.py
class Solution:
    def compress(self, chars: List[str]) -> int:
        N = len(chars)
        prev = chars[0]
        count = 1
        index = 0
        
        for i in range(1, N + 1):
            if i < N and chars[i] == prev:
                count += 1
            else:
                chars[index] = prev
                index += 1
                
                if count != 1:
                    for x in str(count):
                        chars[index] = x
                        index += 1
                
                if i < N:
                    prev, count = chars[i], 1

        return index
```


