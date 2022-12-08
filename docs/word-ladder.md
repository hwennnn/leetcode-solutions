---
id: word-ladder
title: Word Ladder
description: Problem Description and Solution for Word Ladder
sidebar_label: 127. Word Ladder
sidebar_position: 127
---

# [127. Word Ladder](https://leetcode.com/problems/word-ladder/)

```py title=word-ladder.py
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        wordList = set(wordList)
        visited = set([beginWord])
        if endWord not in wordList: return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord: return steps
            
            for i in range(n):
                for c in string.ascii_lowercase:
                    new = word[:i] + c + word[i + 1:]
                    if new in wordList and new not in visited:
                        visited.add(new)
                        queue.append((new, steps + 1))
        
        return 0
```


