---
id: increasing-decreasing-string
title: Increasing Decreasing String
description: Problem Description and Solution for Increasing Decreasing String
sidebar_label: 1370. Increasing Decreasing String
sidebar_position: 1370
---

# [1370. Increasing Decreasing String](https://leetcode.com/problems/increasing-decreasing-string/)

```py title=increasing-decreasing-string.py
class Solution:
    def sortString(self, S: str) -> str:
        mp = collections.defaultdict(int)
        n = len(S)
        for s in S:
            mp[s] += 1
        
        mp = dict(sorted(mp.items()))
        res = []
        while len(res) != n:
            for key in mp:
                if mp[key]:
                    res.append(key)
                    mp[key] -= 1

            for key in dict(sorted(mp.items(), reverse = True)):
                if mp[key]:
                    res.append(key)
                    mp[key] -= 1

        
        return "".join(res)
            
```

```cpp title=increasing-decreasing-string.cpp
class Solution {
public:
    string sortString(string s, string res = "") {
        int cnt[26] = {};
        for (auto ch : s)
            ++cnt[ch - 'a'];
        
        while (res.length() != s.length()){
            for (int i = 0; i < 26; i++)
                res += string(--cnt[i] >= 0 ? 1 : 0, 'a' + i);
            
            for (int i = 25; i >= 0; i--)
                res += string(--cnt[i] >= 0 ? 1 : 0, 'a' + i);
        }
        
        return res;
            
    }
};
```


