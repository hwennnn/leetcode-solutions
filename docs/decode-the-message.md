---
id: decode-the-message
title: Decode the Message
description: Problem Description and Solution for Decode the Message
sidebar_label: 2325. Decode the Message
sidebar_position: 2325
---

# [2325. Decode the Message](https://leetcode.com/problems/decode-the-message/)

```py title=decode-the-message.py
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {}
        
        for x in key:
            if x == " ": continue
                
            if x not in mp:
                mp[x] = chr(ord('a') + len(mp))

        res = ""
        
        for x in message:
            if x == " ":
                res += x
            else:
                res += mp[x]
        
        return res
```


