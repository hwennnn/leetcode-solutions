class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        check = [False] * (n+1)
        check[0] = True
        
        for i in range(n):
            if check[i]:
                for j in range(i, n):
                    if s[i:j+1] in wordDict:
                        check[j+1] = True
        
        return check[-1]
        