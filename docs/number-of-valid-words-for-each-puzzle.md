---
id: number-of-valid-words-for-each-puzzle
title: Number of Valid Words for Each Puzzle
description: Problem Description and Solution for Number of Valid Words for Each Puzzle
sidebar_label: 1178. Number of Valid Words for Each Puzzle
sidebar_position: 1178
---

# [1178. Number of Valid Words for Each Puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/)

```py title=number-of-valid-words-for-each-puzzle.py
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        mp = collections.defaultdict(int)
        res = [0] * len(puzzles)
        
        for word in words:
            mask = 0
            for x in word:
                mask |= (1 << (ord(x) - ord('a')))
            mp[mask] += 1
        
        for i, puzzle in enumerate(puzzles):
            mask = 0
            for x in puzzle:
                mask |= (1 << (ord(x) - ord('a')))
                
            first = 1 << (ord(puzzle[0]) - ord('a'))
            
            sub = mask
            
            while True:
                if (sub & first) == first:
                    res[i] += mp[sub]
                
                if sub == 0: break
                
                sub = (sub - 1) & mask
        
        return res
```


