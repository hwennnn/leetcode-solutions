class Solution:
    def findComplement(self, N: int) -> int:
        X = 1
        while N > X:
            X = X*2 + 1

        return X - N