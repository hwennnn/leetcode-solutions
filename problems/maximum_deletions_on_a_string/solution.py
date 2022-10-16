class Hashes:
    def __init__(self, s, base = 131, mod = 10 ** 9 + 7) -> None:
        self.s = s
        self.base = base
        self.mod = mod
        self.powers = [1]
        self.psa = [0]
        
        for i in range(len(s)):
            self.powers.append(self.powers[-1] * self.base % self.mod)
            self.psa.append((self.psa[-1] + ord(s[i]) * self.powers[-1]) % self.mod)
    
    def get(self, l, r):
        return (self.psa[r + 1] - self.psa[l]) * self.powers[len(self.s) - r] % self.mod

class Solution:
    def deleteString(self, s: str) -> int:
        N = len(s)
        if len(set(s)) == 1: return N
        
        dp = [1] * N
        h = Hashes(s)
        
        for i in range(N - 1, -1, -1):
            for j in range(1, N):
                if i + 2 * j > N: break
                    
                if 1 + dp[i+j] > dp[i] and h.get(i, i + j - 1) == h.get(i + j, i + 2 * j - 1):
                    dp[i] = 1 + dp[i+j]

        return dp[0]