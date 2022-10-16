class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeroes = [0]
        ones = [0]
        
        for x in nums:
            zeroes.append(zeroes[-1] + int(x == 0))
            ones.append(ones[-1] + int(x == 1))

        mp = collections.defaultdict(list)
        res = 0
        
        for i in range(n + 1):
            left = zeroes[i] - zeroes[0]
            right = ones[-1] - ones[i]
            
            count = left + right

            mp[count].append(i)
            res = max(res, count)
        
        return mp[res]