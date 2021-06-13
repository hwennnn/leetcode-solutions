class TrieNode:
    def __init__(self):
        self.pos = -1
        self.nodes = [None] * 26
        self.palins = []

class Solution:    
    def add(self, root, word, pos):
        for i in range(len(word) - 1, -1, -1):
            if self.isPalindrome(word, 0, i):
                root.palins.append(pos)
        
            p = ord(word[i]) - ord('a')
            if not root.nodes[p]:
                root.nodes[p] = TrieNode()
            
            root = root.nodes[p]
        
        root.pos = pos
        root.palins.append(pos)
    
    def isPalindrome(self, word, i, j):
        while i < j and word[i] == word[j]:
            i += 1; j -= 1
            
        return i >= j
    
    def search(self, root, word, pos, res):
        n = len(word)
        j = 0
        
        while root and j < n:
            if root.pos >= 0 and pos != root.pos and self.isPalindrome(word, j, n - 1):
                res.append([pos, root.pos])
            
            p = ord(word[j]) - ord('a')
            root = root.nodes[p]
            j += 1
        
        if root and root.palins:
            for j in root.palins:
                if j != pos:
                    res.append([pos, j])
        
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        root = TrieNode()
        res = []
        
        for i in range(n):
            self.add(root, words[i], i)
        
        for i in range(n):
            self.search(root, words[i], i, res)
        
        return res