class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        res = 0
        
        n = len(word)
        
        for i in range(n):
            A = [0, 0, 0, 0, 0]
            for j in range(i, n):
                if word[j] == 'a':
                    A[0] += 1
                elif word[j] == 'e':
                    A[1] += 1
                elif word[j] == 'i':
                    A[2] += 1
                elif word[j] == 'o':
                    A[3] += 1
                elif word[j] == 'u':
                    A[4] += 1
                else:
                    break
                
                if all(x > 0 for x in A):
                    res += 1

        return res