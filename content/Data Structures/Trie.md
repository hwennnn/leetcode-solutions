---
title: Trie
tags:
  - data-structures
  - trie
  - tree
date: 2023-11-13
---

## Introduction

A **trie** is a tree-like data structure that stores a dynamic set of strings, where the keys are usually strings. In practice, tries are used to facilitate operations on strings, such as searching and prefix matching.

## Implementation

### Dictionary Implementation

```py
class Trie:
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def delete(self, word, prune=False):
        current_dict = self.root
        nodes = [current_dict]
        objects = []
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
            objects.append(current_dict)

        del current_dict["_end_"]

        if prune:
            # https://leetcode.com/problems/maximum-genetic-difference-query/discuss/1344900/
            for c, obj in zip(word[::-1], objects[:-1][::-1]):
                if not obj[c]:
                    del obj[c]
                else:
                    break

        # assert word not in self  # confirm that the number has been removed
```

### Defaultdict Implementation

```py
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.hasEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for x in word:
            curr = curr.children[x]

        curr.hasEnd = True

    def search(self, word: str) -> bool:
        curr = self.root

        for x in word:
            if x not in curr.children:
                return False

            curr = curr.children[x]

        return curr.hasEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for x in prefix:
            if x not in curr.children:
                return False

            curr = curr.children[x]

        return True
```
