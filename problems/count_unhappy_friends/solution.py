class Solution:
    def unhappyFriends(self, n: int, pref: List[List[int]], pairs: List[List[int]]) -> int:
        res = set()
        
		# helper function to check for happiness
        def checkHappiness(x,y,u,v):
             if rank[x][u] < rank[x][y] and rank[u][x] < rank[u][v]:
                res.add(x)
                res.add(u)
				
		# store the pref according in map with index
        rank = [{v:i for i,v in enumerate(row)} for row in pref] 
        
        for i in range(n//2):
            x, y = pairs[i]
            for j in range(i+1, n//2):
                    u,v = pairs[j]
					# loop through permutations of pairs
                    checkHappiness(x, y, u, v)
                    checkHappiness(y, x, u, v)
                    checkHappiness(x, y, v, u)
                    checkHappiness(y, x, v, u)
                    
        return len(res)