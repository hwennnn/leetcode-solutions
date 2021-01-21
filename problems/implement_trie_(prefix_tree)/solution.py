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
        

    def insert(self, word: str) -> None:
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
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        n = len(word)
        for i in range(n):
            index = ord(word[i]) - ord('a')
            if not curr.mp[index]: return False
            
            curr = curr.mp[index]
        
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        n = len(prefix)
        for i in range(n):
            index = ord(prefix[i]) - ord('a')
            if not curr.mp[index]: return False
            
            curr = curr.mp[index]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)