---
id: unique-email-addresses
title: Unique Email Addresses
description: Problem Description and Solution for Unique Email Addresses
sidebar_label: 929. Unique Email Addresses
sidebar_position: 929
---

# [929. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/)

```py title=unique-email-addresses.py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        
        for email in emails:
            email, provider = email.split("@")
            curr = ""
            
            for x in email:
                if x == ".": continue
                if x == "+": break
                
                curr += x
            
            s.add(curr + "@" + provider)
        
        return len(s)
```


