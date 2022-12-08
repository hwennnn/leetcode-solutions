---
id: reorder-data-in-log-files
title: Reorder Data in Log Files
description: Problem Description and Solution for Reorder Data in Log Files
sidebar_label: 937. Reorder Data in Log Files
sidebar_position: 937
---

# [937. Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)

```py title=reorder-data-in-log-files.py
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        
        for index, log in enumerate(logs):
            space = log.index(" ")
            content = log[space + 1:]
            d = log[:space]
            
            if any(digit in content for digit in "1234567890"):
                dig.append(log)
            else:
                let.append((content, d, index))
        
        return [logs[index] for _, __, index in sorted(let)] + dig
```


