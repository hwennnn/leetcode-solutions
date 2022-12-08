---
id: find-the-index-of-the-first-occurrence-in-a-string
title: Find the Index of the First Occurrence in a String
description: Problem Description and Solution for Find the Index of the First Occurrence in a String
sidebar_label: 28. Find the Index of the First Occurrence in a String
sidebar_position: 28
---

# [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)

```py title=find-the-index-of-the-first-occurrence-in-a-string.py
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle: return 0
        
        n = len(needle)
        s = deque()
        
        for index, x in enumerate(haystack):
            if len(s) < n:
                s.append(x)
            
            if len(s) == n:
                word = "".join(s)
                if word == needle:
                    return index - n + 1
                
                s.popleft()
        
        return -1
```

```java title=find-the-index-of-the-first-occurrence-in-a-string.java
class Solution {
   public int strStr(String haystack, String needle) {
      for (int i = 0; ; i++) {
        for (int j = 0; ; j++) {
          if (j == needle.length()) return i;
          if (i + j == haystack.length()) return -1;
          if (needle.charAt(j) != haystack.charAt(i + j)) break;
        }
      }
    }
}
```


