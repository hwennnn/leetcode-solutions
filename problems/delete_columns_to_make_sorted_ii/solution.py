class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        words = ["" for x in strs]
        res = 0
        
        for i in range(n):
            for index, word in enumerate(strs):
                words[index] += word[i]
            
            if any(A > B for A, B in zip(words, words[1:])):
                res += 1
                for index in range(m):
                    words[index] = words[index][:-1]
        
        return res