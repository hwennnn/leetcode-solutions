---
id: defanging-an-ip-address
title: Defanging an IP Address
description: Problem Description and Solution for Defanging an IP Address
sidebar_label: 1108. Defanging an IP Address
sidebar_position: 1108
---

# [1108. Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/)

```py title=defanging-an-ip-address.py
class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = address.replace('.', '[.]')
        
        return address
```


