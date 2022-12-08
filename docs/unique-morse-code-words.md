---
id: unique-morse-code-words
title: Unique Morse Code Words
description: Problem Description and Solution for Unique Morse Code Words
sidebar_label: 804. Unique Morse Code Words
sidebar_position: 804
---

# [804. Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/)

```py title=unique-morse-code-words.py
table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        seen = set()
        
        for word in words:
            s = []
            
            for char in word:
                o = ord(char) - ord("a")
                s.append(table[o])
            
            seen.add("".join(s))
        
        return len(seen)
```


