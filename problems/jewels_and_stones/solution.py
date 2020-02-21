class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        return sum([i in J for i in S])