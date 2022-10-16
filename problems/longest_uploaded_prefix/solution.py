class LUPrefix:

    def __init__(self, n: int):
        self.N = n
        self.dp = [False] * (n + 1)
        self.dp[0] = True
        self.curr = 0

    def upload(self, video: int) -> None:
        self.dp[video] = True
        while self.curr + 1 <= self.N and self.dp[self.curr + 1]:
            self.curr += 1

    def longest(self) -> int:
        return self.curr


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()