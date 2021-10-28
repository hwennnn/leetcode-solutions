class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        M = 10 ** 9 + 7
        counter = collections.Counter(arr)
        res = 0
        
        for i, j in combinations_with_replacement(counter, 2):
            k = target - i - j
            
            if i == j == k:
                res += (counter[i] * (counter[i] - 1) * (counter[i] - 2)) // 6
            elif i == j != k:
                res += (counter[i] * (counter[i] - 1) // 2) * counter[k]
            elif k > i and k > j:
                res += counter[i] * counter[j] * counter[k]
        
        return res % M