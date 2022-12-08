---
id: number-of-times-binary-string-is-prefix-aligned
title: Number of Times Binary String Is Prefix-Aligned
description: Problem Description and Solution for Number of Times Binary String Is Prefix-Aligned
sidebar_label: 1375. Number of Times Binary String Is Prefix-Aligned
sidebar_position: 1375
---

# [1375. Number of Times Binary String Is Prefix-Aligned](https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/)

```py title=number-of-times-binary-string-is-prefix-aligned.py
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        blues = [False] * n
        ons = [False] * n
        res = 0
        on = 0
        for i, x in enumerate(light):
            ons[x-1] = True
            # if idx == 0, then light it up to blue
            if x == 1 or blues[x-2]: 
                blues[x-1] = True

            r = x
            if blues[x-1]:
                while r < n and ons[r]:
                    blues[r] = True
                    on -= 1
                    r += 1
            else:
                on += 1
            
            if on == 0:
                res += 1
            
        return res
            
```

```cpp title=number-of-times-binary-string-is-prefix-aligned.cpp
class Solution {
public:
    int numTimesAllBlue(vector<int>& light) {
        int right = 0, res = 0;

        for (int i = 0; i < light.size(); i++){
            right = max(right, light[i]);
            res += (right == i + 1);
        }
        
        return res;
    }
};
```


