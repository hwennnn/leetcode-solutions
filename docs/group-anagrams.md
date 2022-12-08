---
id: group-anagrams
title: Group Anagrams
description: Problem Description and Solution for Group Anagrams
sidebar_label: 49. Group Anagrams
sidebar_position: 49
---

# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

```py title=group-anagrams.py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        
        for word in strs:
            cnt = [0] * 26
            
            for char in word:
                cnt[ord(char) - ord("a")] += 1
            
            mp[tuple(cnt)].append(word)
        
        return mp.values()
```


