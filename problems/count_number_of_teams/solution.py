class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(len(rating)):
            ls = rs = lb = rb = 0
            
            for j in range(i-1,-1,-1):
                if rating[j] < rating[i]:
                    ls += 1
                elif rating[j] > rating[i]:
                    lb += 1
            
            for j in range(i+1,len(rating)):
                if rating[j] > rating[i]:
                    rb += 1
                elif rating[j] < rating[i]:
                    rs += 1

            res += ls*rb + lb*rs
        return res
            