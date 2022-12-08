---
id: crawler-log-folder
title: Crawler Log Folder
description: Problem Description and Solution for Crawler Log Folder
sidebar_label: 1598. Crawler Log Folder
sidebar_position: 1598
---

# [1598. Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/)

```py title=crawler-log-folder.py
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        
        for log in logs:
            if log == "./":
                continue
            # if depth > 0:
            if depth > 0:
                if log == "../":
                    depth -= 1
                    continue
            
            if log != "../" and log != "./":
                depth += 1
        
        return depth
                
                
                
```


