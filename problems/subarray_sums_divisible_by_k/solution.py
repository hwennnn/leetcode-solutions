class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        s = 0
        mp = defaultdict(int)
        mp[0] = 1

        for x in nums:
            s = (s + x) % k
            res += mp[s]
            mp[s] += 1

        return res