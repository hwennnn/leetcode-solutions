---
id: largest-merge-of-two-strings
title: Largest Merge Of Two Strings
description: Problem Description and Solution for Largest Merge Of Two Strings
sidebar_label: 1754. Largest Merge Of Two Strings
sidebar_position: 1754
---

# [1754. Largest Merge Of Two Strings](https://leetcode.com/problems/largest-merge-of-two-strings/)

```py title=largest-merge-of-two-strings.py
class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = ""
        
        while word1 and word2:
            if word1 >= word2:
                res += word1[0]
                word1 = word1[1:]
            else:
                res += word2[0]
                word2 = word2[1:]
        
        res += word1 or word2
        
        return res
```

```cpp title=largest-merge-of-two-strings.cpp
class Solution {
public:
    string largestMerge(string s, string t) {
        string ans;
        int i = 0, j = 0;
        while(i < s.size() && j < t.size()) {
            if(s.substr(i) >= t.substr(j)) {
                ans += s[i];
                ++i;
            } else {
                ans += t[j];
                ++j;
            }
        }
        while(i < s.size()) {
            ans += s[i];
            ++i;
        }
        while(j < t.size()) {
            ans += t[j];
            ++j;
        }
        return ans;
    }
};

```


