class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        mp = collections.defaultdict(int)
        res = [0] * len(puzzles)
        
        for word in words:
            mask = 0
            for x in word:
                mask |= (1 << (ord(x) - ord('a')))
            mp[mask] += 1
        
        for i, puzzle in enumerate(puzzles):
            mask = 0
            for x in puzzle:
                mask |= (1 << (ord(x) - ord('a')))
                
            first = 1 << (ord(puzzle[0]) - ord('a'))
            
            sub = mask
            
            while True:
                if (sub & first) == first:
                    res[i] += mp[sub]
                
                if sub == 0: break
                
                sub = (sub - 1) & mask
        
        return res