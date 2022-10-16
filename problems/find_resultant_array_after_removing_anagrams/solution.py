class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        while len(words) >= 2:
            currN = len(words)
            
            for i in range(1, len(words)):
                if sorted(words[i - 1]) == sorted(words[i]):
                    words.pop(i)
                    break
            
            if currN == len(words):
                break
                
        
        return words