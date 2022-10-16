class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.value = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, key, val):
        curr = self.root
        
        for c in key:
            curr = curr.children[c]
        
        curr.value = val
    
    def sumVal(self, prefix):
        curr = self.root
        
        for c in prefix:
            curr = curr.children[c]
        
        return self.dfs(curr)
    
    def dfs(self, curr):
        total = curr.value
        
        for char in curr.children:
            if curr.children[char]:
                total += self.dfs(curr.children[char])
        
        return total
    
class MapSum:

    def __init__(self):
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.sumVal(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)