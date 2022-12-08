---
id: clumsy-factorial
title: Clumsy Factorial
description: Problem Description and Solution for Clumsy Factorial
sidebar_label: 1006. Clumsy Factorial
sidebar_position: 1006
---

# [1006. Clumsy Factorial](https://leetcode.com/problems/clumsy-factorial/)

```cpp title=clumsy-factorial.cpp
class Solution {
public:
    int clumsy(int n) {
        stack<int> s;
        s.push(n--);
        
        while (n > 0) {
            int top = s.top();
            s.pop();
            s.push(top * n--);
            
            if (n > 0) {
                int top = s.top();
                s.pop();
                s.push(top / n--);
            }
            
            if (n > 0) {
                s.push(n--);
            }
            
            if (n > 0) {
                s.push(-1 * n--);
            }
        }
        
        int res = 0;
        
        while (s.size() > 0) {
            int top = s.top();
            s.pop();
            res += top;
        }
        
        return res;
    }
};
```


