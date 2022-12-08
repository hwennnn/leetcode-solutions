---
id: apply-discount-to-prices
title: Apply Discount to Prices
description: Problem Description and Solution for Apply Discount to Prices
sidebar_label: 2288. Apply Discount to Prices
sidebar_position: 2288
---

# [2288. Apply Discount to Prices](https://leetcode.com/problems/apply-discount-to-prices/)

```py title=apply-discount-to-prices.py
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def getDiscount(x):
            if discount == 100: return "0.00"
            res = float(x) * float(1 - discount / 100)
            
            return "{:.2f}".format(res)
        
        res = []
        
        for x in sentence.split(" "):
            if x[0] != "$":
                res.append(x)
            else:
                count = 0
                
                for c in x:
                    if c == "$":
                        count += 1
                    elif c in string.ascii_lowercase:
                        count += 1
                
                if len(x) > 1 and x[0] == "$" and count == 1:
                    res.append(x[0] + str(getDiscount(x[1:])))
                else:
                    res.append(x)
        
        return " ".join(res)
```


