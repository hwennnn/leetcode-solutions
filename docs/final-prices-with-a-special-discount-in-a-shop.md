---
id: final-prices-with-a-special-discount-in-a-shop
title: Final Prices With a Special Discount in a Shop
description: Problem Description and Solution for Final Prices With a Special Discount in a Shop
sidebar_label: 1475. Final Prices With a Special Discount in a Shop
sidebar_position: 1475
---

# [1475. Final Prices With a Special Discount in a Shop](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/)

```py title=final-prices-with-a-special-discount-in-a-shop.py
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
    
        for i,price in enumerate(prices):
            
            while stack and prices[stack[-1]] >= price:
                prices[stack.pop()] -= price
                
            stack.append(i)
            
        return prices
```


