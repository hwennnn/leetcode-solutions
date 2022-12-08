---
id: triples-with-bitwise-and-equal-to-zero
title: Triples with Bitwise AND Equal To Zero
description: Problem Description and Solution for Triples with Bitwise AND Equal To Zero
sidebar_label: 982. Triples with Bitwise AND Equal To Zero
sidebar_position: 982
---

# [982. Triples with Bitwise AND Equal To Zero](https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/)

```py title=triples-with-bitwise-and-equal-to-zero.py
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        mp = collections.defaultdict(int)
        res = 0
        
        for a in nums:
            for b in nums:
                mp[a & b] += 1
        
        for c in nums:
            for ab in mp:
                if ab & c == 0:
                    res += mp[ab]
        
        return res
```


