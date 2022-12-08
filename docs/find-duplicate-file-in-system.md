---
id: find-duplicate-file-in-system
title: Find Duplicate File in System
description: Problem Description and Solution for Find Duplicate File in System
sidebar_label: 609. Find Duplicate File in System
sidebar_position: 609
---

# [609. Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/)

```py title=find-duplicate-file-in-system.py
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        
        for path in paths:
            firstSpace = path.index(" ")
            directory, files = path[:firstSpace], path[firstSpace:].strip().split(" ")
            
            for file in files:
                fileName, content = file.split("(")
                content = content[:-1]
                
                contents[content].append(directory + "/" + fileName)
    
        return [content for content in contents.values() if len(content) > 1]
```


