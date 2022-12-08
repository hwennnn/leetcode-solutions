---
id: search-suggestions-system
title: Search Suggestions System
description: Problem Description and Solution for Search Suggestions System
sidebar_label: 1268. Search Suggestions System
sidebar_position: 1268
---

# [1268. Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

```py title=search-suggestions-system.py
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        mp = defaultdict(list)
        products.sort()
        
        for product in products:
            curr = ""
            
            for x in product:
                curr += x
                if len(mp[curr]) == 3: continue
                mp[curr].append(product)
        
        res = []
        curr = ""
        for word in searchWord:
            curr += word
            res.append(mp[curr][:3])
        
        return res
```


