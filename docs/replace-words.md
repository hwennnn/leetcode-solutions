---
id: replace-words
title: Replace Words
description: Problem Description and Solution for Replace Words
sidebar_label: 648. Replace Words
sidebar_position: 648
---

# [648. Replace Words](https://leetcode.com/problems/replace-words/)

```py title=replace-words.py
class TrieNode:
    def __init__(self):
        self.mp = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.ans = collections.defaultdict(int)


    def insert(self, word: str):
        """
        Inserts a word into the trie.
        """
        curr = self.root
        n = len(word)
        for i in range(n):
            index = ord(word[i]) - ord('a')
            if not curr.mp[index]:
                curr.mp[index] = TrieNode()

            curr = curr.mp[index]

        curr.end = True
        
    def search(self, word: str):
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        n = len(word)
        for i in range(n):
            index = ord(word[i]) - ord('a')
            if not curr.mp[index]: return word
            if curr.mp[index].end: return word[:i+1]

            curr = curr.mp[index]

        return word
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str):
        trie = Trie()
        
        for word in dictionary:
            trie.insert(word)
        
        res = []
        sentence = sentence.split()
        for s in sentence:
            res.append(trie.search(s))
        
        return " ".join(res)
        
        
```


