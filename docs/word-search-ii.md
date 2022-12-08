---
id: word-search-ii
title: Word Search II
description: Problem Description and Solution for Word Search II
sidebar_label: 212. Word Search II
sidebar_position: 212
---

# [212. Word Search II](https://leetcode.com/problems/word-search-ii/)

```py title=word-search-ii.py
class TrieNode:
    
    def __init__(self):
        self.hasWord = False
        self.children = collections.defaultdict(TrieNode)
    
    def hasEdge(self, char: str) -> bool:
        return char in self.children
    
    def get(self, char):
        return self.children[char]

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for w in word:
            curr = curr.children[w]
        
        curr.hasWord = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        trie = Trie()
        res = set()
        visited = set()
        
        for word in words:
            trie.insert(word)
        
        def go(x, y, curr, node):
            if node.hasWord:
                res.add(curr)
            
            for dx, dy in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= dx < rows and 0 <= dy < cols and (dx, dy) not in visited and node.hasEdge(board[dx][dy]):
                    visited.add((dx, dy))
                    go(dx, dy, curr + board[dx][dy], node.get(board[dx][dy]))
                    visited.remove((dx, dy))
            
        for x in range(rows):
            for y in range(cols):
                if trie.root.hasEdge(board[x][y]):
                    visited.add((x, y))
                    go(x, y, board[x][y], trie.root.get(board[x][y]))
                    visited.remove((x, y))
        
        return list(res)
```

```cpp title=word-search-ii.cpp
class Solution {
    struct TrieNode {
        TrieNode *children[26];
        string word;

        TrieNode() : word("") {
            for (int i = 0; i < 26; i++) {
                children[i] = nullptr;
            }
        }
    };

public:
    vector<string> findWords(vector<vector<char>> &board, vector<string> &words) {
        TrieNode *root = buildTrie(words);
        vector<string> result;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(board, i, j, root, result);
            }
        }
        return result;
    }

    /** Inserts a word into the trie. */
    TrieNode *buildTrie(vector<string> &words) {
        TrieNode *root = new TrieNode();
        for (int j = 0; j < words.size(); j++) {
            string word = words[j];
            TrieNode *curr = root;
            for (int i = 0; i < word.length(); i++) {
                char c = word[i] - 'a';
                if (curr->children[c] == nullptr) {
                    curr->children[c] = new TrieNode();
                }
                curr = curr->children[c];
            }
            curr->word = word;
        }
        return root;
    }

    void dfs(vector<vector<char>> &board, int i, int j, TrieNode *p, vector<string> &result) {
        char c = board[i][j];
        if (c == '#' || !p->children[c - 'a']) return;
        p = p->children[c - 'a'];
        if (p->word.size() > 0) {
            result.push_back(p->word);
            p->word = "";
        }

        board[i][j] = '#';
        if (i > 0) dfs(board, i - 1, j, p, result);
        if (j > 0) dfs(board, i, j - 1, p, result);
        if (i < board.size() - 1) dfs(board, i + 1, j, p, result);
        if (j < board[0].size() - 1) dfs(board, i, j + 1, p, result);
        board[i][j] = c;
    }
};
```


