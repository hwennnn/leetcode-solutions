class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        A = sorted([a, b, c])
        a, b, c = A
        if c - a == 2: return [0, 0]
        return [1 if min(c - b, b - a) <= 2 else 2, c - a - 2]