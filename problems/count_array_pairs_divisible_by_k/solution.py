class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        divisors = []
        count = Counter()
        
        for x in range(1, k + 1):
            if k % x == 0:
                divisors.append(x)
        
        for x in nums:
            remainder = k // math.gcd(k, x)
            res += count[remainder]
            
            for divisor in divisors:
                if x % divisor == 0:
                    count[divisor] += 1
        
        return res