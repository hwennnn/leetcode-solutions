---
id: valid-parenthesis-string
title: Valid Parenthesis String
description: Problem Description and Solution for Valid Parenthesis String
sidebar_label: 678. Valid Parenthesis String
sidebar_position: 678
---

# [678. Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)

```py title=valid-parenthesis-string.py
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0

```

```java title=valid-parenthesis-string.java
class Solution {
   public boolean checkValidString(String s) {
        int low = 0;
        int high = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                low++;
                high++;
            } else if (s.charAt(i) == ')') {
                if (low > 0) {
                    low--;
                }
                high--;
            } else {
                if (low > 0) {
                    low--;
                }
                high++;
            }
            if (high < 0) {
                return false;
            }
        }
        return low == 0;
    }
}
```


