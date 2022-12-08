---
id: valid-number
title: Valid Number
description: Problem Description and Solution for Valid Number
sidebar_label: 65. Valid Number
sidebar_position: 65
---

# [65. Valid Number](https://leetcode.com/problems/valid-number/)

```py title=valid-number.py
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        pointSeen = eSeen = numberSeen = False
        
        for i,x in enumerate(s):
            if x >= '0' and x <= '9':
                numberSeen = True
            elif x == '.':
                if pointSeen or eSeen: return False
                pointSeen = True
            elif x == 'e' or x == 'E':
                if eSeen or not numberSeen: return False
                eSeen = True
                numberSeen = False
            elif x == '+' or x == '-':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E': return False
            else:
                return False
        
        return numberSeen

```

```java title=valid-number.java
class Solution {
    public boolean isNumber(String s) {
        s = s.trim();
        boolean pointSeen = false;
        boolean eSeen = false;
        boolean numberSeen = false;
        
        for (int i=0; i<s.length(); i++) {
            if('0' <= s.charAt(i) && s.charAt(i) <= '9') {
                numberSeen = true;
            } else if(s.charAt(i) == '.') {
                if(eSeen || pointSeen)
                    return false;
                pointSeen = true;
            } else if(s.charAt(i) == 'e' || s.charAt(i) == 'E') {
                if(eSeen || !numberSeen)
                    return false;
                numberSeen = false;
                eSeen = true;
            } else if(s.charAt(i) == '-' || s.charAt(i) == '+') {
                if(i != 0 && s.charAt(i-1) != 'e' && s.charAt(i-1) != 'E')
                    return false;
            } else
                return false;
        }
        
        return numberSeen;
    }
}
```


