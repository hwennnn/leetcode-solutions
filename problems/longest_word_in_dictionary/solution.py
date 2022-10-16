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
        
    def search(self):
        self.searchR(self.root)

    def searchR(self, node, word = "", level = 0):
        """
        Returns if the word is in the trie.
        """
        
        if node.end and not self.ans[level]:
            self.ans[level] = word
        
        if self.isLastNode(node): return
        
        for i in range(26):
            if node.mp[i] and node.mp[i].end: 
                word += chr(97+i)
                self.searchR(node.mp[i], word, level + 1)
                word = word[:-1]
    
    def isLastNode(self, node):
        for i in range(26):
            if node.mp[i]: return False
        
        return True
        


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        
        for w in words:
            trie.insert(w)
        
        trie.search()
        res = trie.ans
        
        return res[max(res)]
        
        