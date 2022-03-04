class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        return sorted(range(1, N + 1), key = lambda x : bin(x)[:1:-1])