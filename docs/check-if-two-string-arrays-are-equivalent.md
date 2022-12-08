---
id: check-if-two-string-arrays-are-equivalent
title: Check If Two String Arrays are Equivalent
description: Problem Description and Solution for Check If Two String Arrays are Equivalent
sidebar_label: 1662. Check If Two String Arrays are Equivalent
sidebar_position: 1662
---

# [1662. Check If Two String Arrays are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/)

```py title=check-if-two-string-arrays-are-equivalent.py
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n1, n2 = len(word1), len(word2)
        i = j = ki = kj = 0
        
        while i < n1 and j < n2:
            while ki < len(word1[i]) and kj < len(word2[j]):
                if word1[i][ki] != word2[j][kj]:
                    return False
                
                ki += 1
                kj += 1
            
            if ki == len(word1[i]):
                i += 1
                ki = 0
            
            if kj == len(word2[j]):
                j += 1
                kj = 0
        
        return i == n1 and j == n2
```

```cpp title=check-if-two-string-arrays-are-equivalent.cpp
class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1 = "", s2 = "";
        for (auto w : word1) s1 += w;
        for (auto w: word2) s2 += w;
        
        return s1 == s2;
    }
};
```


