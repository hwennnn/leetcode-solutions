---
id: bag-of-tokens
title: Bag of Tokens
description: Problem Description and Solution for Bag of Tokens
sidebar_label: 948. Bag of Tokens
sidebar_position: 948
---

# [948. Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)

```py title=bag-of-tokens.py
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        N = len(tokens)
        curr = res = 0
        i, j = 0, N - 1
        
        while i <= j:
            if power >= tokens[i]:
                curr += 1
                res = max(res, curr)
                power -= tokens[i]
                i += 1
            elif curr > 0:
                curr -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        
        return res
```


