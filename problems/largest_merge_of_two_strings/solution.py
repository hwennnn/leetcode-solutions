class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = ""
        
        while word1 and word2:
            if word1 >= word2:
                res += word1[0]
                word1 = word1[1:]
            else:
                res += word2[0]
                word2 = word2[1:]
        
        res += word1 or word2
        
        return res