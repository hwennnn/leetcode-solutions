---
id: online-stock-span
title: Online Stock Span
description: Problem Description and Solution for Online Stock Span
sidebar_label: 901. Online Stock Span
sidebar_position: 901
---

# [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/)

```py title=online-stock-span.py
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        curr = 1
        
        while self.stack and self.stack[-1][0] <= price:
            prior, streak = self.stack.pop()
            curr += streak
        self.stack.append((price, curr))
        return curr

    
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```


