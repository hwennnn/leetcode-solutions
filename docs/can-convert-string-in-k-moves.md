---
id: can-convert-string-in-k-moves
title: Can Convert String in K Moves
description: Problem Description and Solution for Can Convert String in K Moves
sidebar_label: 1540. Can Convert String in K Moves
sidebar_position: 1540
---

# [1540. Can Convert String in K Moves](https://leetcode.com/problems/can-convert-string-in-k-moves/)

```java title=can-convert-string-in-k-moves.java
class Solution {
   public boolean canConvertString(String s, String t, int k) {
        int[] count = new int[26];
        for (int i = 0; i < Math.min(s.length(), t.length()); ++i) {
            int diff = (t.charAt(i) - s.charAt(i) + 26) % 26;
            if (diff > 0 && diff + count[diff] * 26 > k) {
                return false;
            }
            ++count[diff];
        }
        return s.length() == t.length();
    }
}
```


