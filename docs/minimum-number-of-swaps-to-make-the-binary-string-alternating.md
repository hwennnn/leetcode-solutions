---
id: minimum-number-of-swaps-to-make-the-binary-string-alternating
title: Minimum Number of Swaps to Make the Binary String Alternating
description: Problem Description and Solution for Minimum Number of Swaps to Make the Binary String Alternating
sidebar_label: 1864. Minimum Number of Swaps to Make the Binary String Alternating
sidebar_position: 1864
---

# [1864. Minimum Number of Swaps to Make the Binary String Alternating](https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/)

```py title=minimum-number-of-swaps-to-make-the-binary-string-alternating.py
class Solution:
    def minSwaps(self, s: str) -> int:
        ones = zeroes = 0
        
        for c in s:
            if c == '0':
                zeroes += 1
            else:
                ones += 1
        
        if abs(zeroes - ones) > 1: return -1
        
        def countSwap(char):
            count = 0
            for c in s:
                if c != char:
                    count += 1
                char = '1' if char == '0' else '0'
            
            return count // 2
        
        if zeroes > ones:
            return countSwap('0')
        elif ones > zeroes:
            return countSwap('1')
        else:
            return min(countSwap('0'), countSwap('1'))
```


