class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int) (sqrt(1 + (8 * n)) - 1) // 2
    