class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + int(low & 1 or high & 1)