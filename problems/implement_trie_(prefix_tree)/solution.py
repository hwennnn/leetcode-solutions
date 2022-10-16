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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)