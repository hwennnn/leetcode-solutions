---
id: factorial-trailing-zeroes
title: Factorial Trailing Zeroes
description: Problem Description and Solution for Factorial Trailing Zeroes
sidebar_label: 172. Factorial Trailing Zeroes
sidebar_position: 172
---

# [172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/)

```java title=factorial-trailing-zeroes.java
public class Solution {
    public int trailingZeroes(int n) {
        int count = 0;
        while (n != 0) {
            int tmp = n / 5;
            count += tmp;
            n = tmp;
        }
        return count;
    }
}
```


