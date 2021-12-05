class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.hasWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word[::-1]:
            curr = curr.children[c]
        
        curr.hasWord = True
    
    def hasWord(self, word):
        curr = self.root
        
        for c in word[::-1]:
            if c not in curr.children: return False
            curr = curr.children[c]
            if curr.hasWord:
                return True
        
        return False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.q = ""
        
        for word in words:
            self.trie.insert(word)

    def query(self, letter: str) -> bool:
        self.q += letter
        
        return self.trie.hasWord(self.q)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)