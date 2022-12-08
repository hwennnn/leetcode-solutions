---
id: decrypt-string-from-alphabet-to-integer-mapping
title: Decrypt String from Alphabet to Integer Mapping
description: Problem Description and Solution for Decrypt String from Alphabet to Integer Mapping
sidebar_label: 1309. Decrypt String from Alphabet to Integer Mapping
sidebar_position: 1309
---

# [1309. Decrypt String from Alphabet to Integer Mapping](https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/)

```py title=decrypt-string-from-alphabet-to-integer-mapping.py
class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        i = 0
        res = []
        
        while i < n:
            if i + 2 < n and s[i + 2] == "#":
                c = int(s[i : i + 2]) - 1
                res.append(chr(ord('a') + c))
                i += 3
            else:
                c = int(s[i]) - 1
                res.append(chr(ord('a') + c))
                i += 1
        
        return "".join(res)
```

```cpp title=decrypt-string-from-alphabet-to-integer-mapping.cpp
class Solution {
public:
    string freqAlphabets(string s) {
      string res;
      for (int i = 0; i < s.size(); ++i) {
        if (i < s.size() - 2 && s[i + 2] == '#') {
          res += 'j' + (s[i] - '1') * 10 + s[i + 1] - '0';
          i += 2;
        }
        else res += 'a' + (s[i] - '1');
      }
      return res;
}
};
```


