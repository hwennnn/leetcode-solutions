class Solution:
    def numEquivDominoPairs(self, arr: List[List[int]]) -> int:
        
        n = len(arr)
        dic = {}
        res = 0
        
        for pair in arr:
            num = min(pair[0],pair[1])*10 + max(pair[0],pair[1])
            if num in dic:
                res += dic[num]
                dic[num] += 1
            else:
                dic[num] = 1

        return res
            
                    