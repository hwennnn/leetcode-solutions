class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time = timeToLive
        self.mp = collections.defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.mp:
            self.mp[tokenId] = currentTime + self.time

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.mp and currentTime < self.mp[tokenId]:
            self.mp[tokenId] = currentTime + self.time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        
        for key in self.mp:
            if self.mp[key] > currentTime:
                res += 1
        
        return res


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)