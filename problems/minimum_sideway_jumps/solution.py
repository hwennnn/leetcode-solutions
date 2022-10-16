class Solution:
    def minSideJumps(self, obs: List[int]) -> int:
        n = len(obs)
        lanes = [[True] * n for _ in range(3)]

        for i,x in enumerate(obs):
            if x != 0:
                lanes[x - 1][i] = False
                
        suffix = [[1] * n for _ in range(3)]
        for i in range(3):
            for j in reversed(range(n)):
                if not lanes[i][j]:
                    suffix[i][j] = 0
                else:
                    if j != n - 1:
                        suffix[i][j] += suffix[i][j + 1]
        
        curr = 1
        jumps = 0
        for i in range(n-1):
            if not lanes[curr][i+1]:
                lane1 = suffix[0][i] if curr != 0 and lanes[0][i] else float('-inf')
                lane2 = suffix[1][i] if curr != 1 and lanes[1][i] else float('-inf')
                lane3 = suffix[2][i] if curr != 2 and lanes[2][i] else float('-inf')
                
                m = max(lane1, lane2, lane3)
                if m == lane1: 
                    curr = 0
                elif m == lane2: 
                    curr = 1
                else:
                     curr = 2
                
                jumps += 1

            
        return jumps