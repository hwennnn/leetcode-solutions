class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        N = len(nums)
        res = set()

        for x in nums:
            for k in range(2, int(math.sqrt(x)) + 1):
                if x % k == 0:
                    res.add(k)
                    
                    while x % k == 0:
                        x //= k

            if x >= 2:
                res.add(x)

        return len(set(res))