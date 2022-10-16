class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        count = [0] * 26
        
        for x in letters:
            index = ord(x) - ord("a")
            count[index] += 1
        
        index = ord(target) - ord("a") + 1
        
        for i in range(26):
            if count[(index + i) % 26] > 0:
                return chr(ord("a") + (index + i) % 26)
        
        