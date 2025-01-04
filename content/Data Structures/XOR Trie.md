---
title: XOR Trie
tags:
  - data-structures
  - trie
  - xor
date: 2023-11-13
---

## Introduction

An XOR trie, also known as a binary trie or a bitwise trie, is a data structure used for storing a collection of binary numbers in a way that supports efficient bitwise operations like bitwise XOR. It is particularly useful in solving problems that involve bitwise operations, such as finding the maximum XOR value between two numbers in a given set.

## Implementation

### Array Implementation

```py
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        N = len(nums)
        MAX_BIT = max(nums).bit_length()
        root = [None, None]
        res = 0

        def add(x):
            curr = root

            for k in range(MAX_BIT, -1, -1):
                if x & (1 << k) > 0:
                    bit = 1
                else:
                    bit = 0

                if curr[bit] is None:
                    curr[bit] = [None, None]

                curr = curr[bit]

        def query(x):
            res = 0
            curr = root

            for k in range(MAX_BIT, -1, -1):
                if x & (1 << k) > 0:
                    bit = 1
                else:
                    bit = 0

                opp = 1 - bit

                if curr is not None and curr[opp] is not None:
                    res += (1 << k)
                    curr = curr[opp]
                else:
                    if curr is None:
                        curr = [None, None]
                    curr = curr[bit]

            return res

        for x in nums:
            res = max(res, query(x))
            add(x)

        return res
```

### Classic Trie Implementation

```py
class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self, MAX_BIT):
        self.root = TrieNode()
        self.MAX_BIT = MAX_BIT

    def insert(self, x):
        curr = self.root

        for k in range(self.MAX_BIT, -1, -1):
            if x & (1 << k) %3E 0:
                bit = 1
            else:
                bit = 0

            if curr.children[bit] is None:
                curr.children[bit] = TrieNode()

            curr = curr.children[bit]

    def query(self, x):
        res = 0
        curr = self.root

        for k in range(self.MAX_BIT, -1, -1):
            if x & (1 << k) > 0:
                bit = 1
            else:
                bit = 0

            opp = 1 - bit

            if curr.children[opp] is not None:
                res |= (1 << k)
                curr = curr.children[opp]
            else:
                if curr.children[bit] is None:
                    curr.children[bit] = TrieNode()
                curr = curr.children[bit]

        return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        N = len(nums)
        MAX_BIT = max(nums).bit_length()
        trie = Trie(MAX_BIT)
        res = 0

        for x in nums:
            res = max(req, trie.query(x))
            trie.insert(x)

        return res
```

## Complexity

- Time complexity:
  - ${O(N * L)}$ for building the Trie, where N is the size of the array and L is the average length of the binary representation of the numbers.
  - ${O(L)}$ for the query
- Space complexity:
  - ${O(N * L)}$ for building the Trie
  - ${O(1)}$ for the query

## Resources

1. [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
2. [2935. Maximum Strong Pair XOR II](https://leetcode.com/problems/maximum-strong-pair-xor-ii/description/)
3. [1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)
4. [1803. Count Pairs With XOR in a Range](https://leetcode.com/problems/count-pairs-with-xor-in-a-range/)
