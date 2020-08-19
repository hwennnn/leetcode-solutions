class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        # Brute force n^3
#         n = len(rating)
#         ans = 0
    
#         for i in range(n):
#             for j in range(i+1,n):
#                 for k in range(j+1,n):
#                     ans += (rating[i]< rating[j] < rating[k] or rating[i] > rating[j] > rating[k])
        
#         return ans
                
        # n^2
        n = len(rating)
        res = 0
        
        for i in range(n):
            ls = lb = rs = rb = 0
            for j in range(i-1,-1,-1):
                if rating[j] < rating[i]:
                    ls += 1
                elif rating[j] > rating[i]:
                    lb += 1
            
            for j in range(i+1,n):
                if rating[j] > rating[i]:
                    rb += 1
                elif rating[j] < rating[i]:
                    rs += 1

            res += ls*rb + lb*rs
        
        return res
                
                
                
        