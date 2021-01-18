class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        mp = Counter(nums)
        res = 0
        
        for key in mp:
            if key * 2 == k:
                res += mp[key] // 2
            else:
                t = k - key
                if t < key:
                    res += min(mp[t], mp[key])

        return res