class TrieNode:
    def __init__(self):
        self.mp = [None] * 26
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = collections.defaultdict(int)

    def insert(self, word: str):
        curr = self.root
        n = len(word)
        for i in range(n):
            index = ord(word[i]) - ord('a')
            if not curr.mp[index]:
                curr.mp[index] = TrieNode()

            curr = curr.mp[index]

        curr.end = True
        
    def search(self, word: str):
        res = []
        
        curr = self.root
        n = len(word)
        for i in range(n):
            index = ord(word[i]) - ord('a')
            if not curr.mp[index]: return res
            
            curr = curr.mp[index]

        self.searchR(curr, word, res)
        
        return res
    
    def searchR(self, node, word, res):
        if len(res) == 3: return
        
        if node.end: res.append(word)
        
        if self.isLastNode(node): return
        
        for i in range(26):
            if node.mp[i]:
                word += chr(97+i)
                self.searchR(node.mp[i], word, res)
                word = word[:-1]
        
    
    def isLastNode(self, node):
        for i in range(26):
            if node.mp[i]: return False

        return True
        
             
class Solution:
    def suggestedProducts(self, products: List[str], word: str) -> List[List[str]]:
        trie = Trie()
        
        for w in products: trie.insert(w)
        
        res = []
        n = len(word)
        
        for i in range(n):
            w = word[:i+1]
            res.append(trie.search(w))
        
        return res