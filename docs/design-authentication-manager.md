---
id: design-authentication-manager
title: Design Authentication Manager
description: Problem Description and Solution for Design Authentication Manager
sidebar_label: 1797. Design Authentication Manager
sidebar_position: 1797
---

# [1797. Design Authentication Manager](https://leetcode.com/problems/design-authentication-manager/)

```py title=design-authentication-manager.py
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.expiredTime = timeToLive
        self.tokens = defaultdict(int)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.expiredTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens or currentTime >= self.tokens[tokenId]: return
        
        self.tokens[tokenId] = currentTime + self.expiredTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        
        for x in self.tokens:
            if self.tokens[x] > currentTime:
                res += 1
        
        return res


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
```


