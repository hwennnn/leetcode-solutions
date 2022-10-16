class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(A) for A in accounts)