table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        seen = set()
        
        for word in words:
            s = []
            
            for char in word:
                o = ord(char) - ord("a")
                s.append(table[o])
            
            seen.add("".join(s))
        
        return len(seen)