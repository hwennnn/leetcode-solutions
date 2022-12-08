---
id: time-needed-to-buy-tickets
title: Time Needed to Buy Tickets
description: Problem Description and Solution for Time Needed to Buy Tickets
sidebar_label: 2073. Time Needed to Buy Tickets
sidebar_position: 2073
---

# [2073. Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/)

```py title=time-needed-to-buy-tickets.py
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        
        for i in range(len(tickets)):
            if i <= k:
                res += min(tickets[k], tickets[i])
            else:
                res += min(tickets[k] - 1, tickets[i])
        
        return res
```


