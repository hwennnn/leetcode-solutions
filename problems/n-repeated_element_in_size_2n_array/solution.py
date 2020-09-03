class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        B = set(A)
        return (sum(A) - sum(B)) // (len(A) - len(B))