---
id: filling-bookcase-shelves
title: Filling Bookcase Shelves
description: Problem Description and Solution for Filling Bookcase Shelves
sidebar_label: 1105. Filling Bookcase Shelves
sidebar_position: 1105
---

# [1105. Filling Bookcase Shelves](https://leetcode.com/problems/filling-bookcase-shelves/)

```py title=filling-bookcase-shelves.py
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        
        for i, (width, height) in enumerate(books, 1):
            dp[i] = dp[i - 1] + height
            
            j = i - 1
            while j > 0 and books[j - 1][0] + width <= shelf_width:
                height = max(height, books[j - 1][1])
                width += books[j - 1][0]
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1
            
        return dp[-1]
```


