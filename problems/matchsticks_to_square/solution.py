class Solution:
    def makesquare(self, sticks: List[int]) -> bool:
        n = len(sticks)
        ssum = sum(sticks)
        target = ssum // 4
        
        if ssum % 4 != 0: return False
        
        sticks.sort(reverse = 1)
        
        def go(curr, index):
            if index == n: return True
                      
            for i in range(4):
                if curr[i] + sticks[index] > target: continue
                
                curr[i] += sticks[index]
                if go(curr, index + 1): return True
                curr[i] -= sticks[index]
        
        return go([0,0,0,0], 0)