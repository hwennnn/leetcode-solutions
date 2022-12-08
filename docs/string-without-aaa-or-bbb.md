---
id: string-without-aaa-or-bbb
title: String Without AAA or BBB
description: Problem Description and Solution for String Without AAA or BBB
sidebar_label: 984. String Without AAA or BBB
sidebar_position: 984
---

# [984. String Without AAA or BBB](https://leetcode.com/problems/string-without-aaa-or-bbb/)

```py title=string-without-aaa-or-bbb.py
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ""
        
        
        while a > 0 and b > 0:
            if a > b:
                res += "a" * min(a, 2)
                res += "b"
                a -= min(a, 2)
                b -= 1
            elif a == b:
                if not res or res[-1] == "a":
                    res += "b"
                    b -= 1
                else:
                    res += "a"
                    a -= 1
            else:
                res += "b" * min(b, 2)
                res += "a"
                b -= min(b, 2)
                a -= 1
        
        if a > 0:
            res += "a" * a
        
        if b > 0:
            res += "b" * b
        
        return res
```


