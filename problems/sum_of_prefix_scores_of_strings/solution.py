# ----------------------------------- Trie -----------------------------------
class Trie:
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
    def __init__(self, words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
            current_dict["count"] = current_dict.get("count", 0) + 1
            
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

    def query(self, word):
        current_dict = self.root
        total = 0
        
        for letter in word:
            if letter not in current_dict: break
            current_dict = current_dict[letter]
            total += current_dict["count"]
            
        return total
    
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        N = len(words)
        res = [0] * N
        trie = Trie(words)
        
        for index, word in enumerate(words):
            res[index] = trie.query(word)
        
        return res