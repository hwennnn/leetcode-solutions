---
id: product-of-the-last-k-numbers
title: Product of the Last K Numbers
description: Problem Description and Solution for Product of the Last K Numbers
sidebar_label: 1352. Product of the Last K Numbers
sidebar_position: 1352
---

# [1352. Product of the Last K Numbers](https://leetcode.com/problems/product-of-the-last-k-numbers/)

```py title=product-of-the-last-k-numbers.py
class ProductOfNumbers:
    
    def __init__(self):
        self.A = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.A)
        if k >= n : return 0
        
        return self.A[-1] // self.A[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```


