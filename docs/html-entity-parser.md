---
id: html-entity-parser
title: HTML Entity Parser
description: Problem Description and Solution for HTML Entity Parser
sidebar_label: 1410. HTML Entity Parser
sidebar_position: 1410
---

# [1410. HTML Entity Parser](https://leetcode.com/problems/html-entity-parser/)

```py title=html-entity-parser.py
class Solution:
    def entityParser(self, text: str) -> str:
        d = {"&quot;" : '"', 
             "&apos;": "'",
             "&amp;": "&",
             "&gt;":">",
             "&lt;" : "<",
             "&frasl;" : "/"}

        special = ""
        res = ""
        for c in text:
            if c != "&":
                if special == "":
                    res += c
                else:
                    special += c
                    
                    if c == ";":
                        if special in d:
                            res += d[special]
                            special = ""
                        else:
                            res += special
                            special = ""
            else:
                res += special
                special = "&"
            
        return res
```


