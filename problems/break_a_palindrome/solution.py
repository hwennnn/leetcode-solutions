class Solution:
    def breakPalindrome(self, A: str) -> str:
        for i in range(len(A) // 2):
            if A[i] != 'a':
                return A[:i] + 'a' + A[i + 1:]
        
        return A[:-1] + 'b' if A[:-1] else ''