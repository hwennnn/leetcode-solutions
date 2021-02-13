class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.child[char]
        cur.is_word = True

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def find(node, p_i, pattern, cur_word, table):
            if p_i >= len(pattern):
                if node.is_word:
                    key = "".join(cur_word)
                    table[key] = True
                for k in node.child:
                    if k.islower():
                        find(node.child[k], p_i, pattern, cur_word+[k], table)
            else:
                for k in node.child:
                    if k == pattern[p_i]:
                        find(node.child[k], p_i+1, pattern, cur_word+[k], table)
                    elif k.islower():
                        find(node.child[k], p_i, pattern, cur_word+[k], table)
        
        trie = Trie()
        for q in queries:
            trie.insert(q)
        
        table = collections.defaultdict(lambda: False)
        find(trie.root, 0, pattern, [], table)

        return [table[q] for q in queries]