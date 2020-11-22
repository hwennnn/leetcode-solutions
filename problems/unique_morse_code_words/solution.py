class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        s = set()
        
        for word in words:
            w = []
            for c in word:
                w.append(morse[ord(c) - ord('a')])
            
            s.add("".join(w))
        
        return len(s)