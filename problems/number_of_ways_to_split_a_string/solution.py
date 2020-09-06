class Solution:
    def numWays(self, s: str) -> int:
        ones, n = s.count('1'), len(s)
        if ones == 0:
            return (n - 2) * (n - 1) // 2 % (10 ** 9 + 7)
        if ones % 3 != 0:
            return 0
        ones //= 3
        count = lo = hi = 0
        for char in s:
            if char == '1':
                count += 1
            if count == ones:
                lo += 1
            elif count == 2 * ones:
                hi += 1
        return lo * hi % (10 **9 + 7)