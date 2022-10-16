class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        O = {x: i for i, x in enumerate(order)}
        
        words = [[O[x] for x in word] for word in words]
        
        return all(x1 <= x2 for x1, x2 in zip(words, words[1:]))