---
id: remove-sub-folders-from-the-filesystem
title: Remove Sub-Folders from the Filesystem
description: Problem Description and Solution for Remove Sub-Folders from the Filesystem
sidebar_label: 1233. Remove Sub-Folders from the Filesystem
sidebar_position: 1233
---

# [1233. Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)

```py title=remove-sub-folders-from-the-filesystem.py
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key = len)
        s = set()
        res = []
        
        for f in folder:
            path = f.split("/")[1:]
            full = ""
            for p in path:
                full += p
                if full in s: break
            else:
                s.add(full)
                res.append(f)
    
                
        
        return res
```


