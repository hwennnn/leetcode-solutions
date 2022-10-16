class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i - v) <= 1 for i, v in enumerate(A))
