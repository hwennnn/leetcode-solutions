---
id: number-of-steps-to-reduce-a-number-to-zero
title: Number of Steps to Reduce a Number to Zero
description: Problem Description and Solution for Number of Steps to Reduce a Number to Zero
sidebar_label: 1342. Number of Steps to Reduce a Number to Zero
sidebar_position: 1342
---

# [1342. Number of Steps to Reduce a Number to Zero](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)

```py title=number-of-steps-to-reduce-a-number-to-zero.py
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        
        while num > 0:
            res += 1
            
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
        
        return res
```

```cpp title=number-of-steps-to-reduce-a-number-to-zero.cpp
class Solution {
public:
    int numberOfSteps (int num) {
        if (!num) return 0;
        int res = 0;
        
        while (num){
            res += (num&1) ? 2 : 1;
            num >>= 1;
        }
        
        return res - 1;
        
    }
};
```


