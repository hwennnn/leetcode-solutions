---
id: masking-personal-information
title: Masking Personal Information
description: Problem Description and Solution for Masking Personal Information
sidebar_label: 831. Masking Personal Information
sidebar_position: 831
---

# [831. Masking Personal Information](https://leetcode.com/problems/masking-personal-information/)

```py title=masking-personal-information.py
class Solution:
    def maskPII(self, s: str) -> str:
        a = s.find("@")
        
        if a != -1:
            return (s[0] + "*" * 5 + s[a - 1:]).lower()
        
        digits = "".join([x for x in s if x.isdigit()])

        return ["", "+*-", "+**-", "+***-"][len(digits) - 10] + "***-***-" + digits[-4:]
```


