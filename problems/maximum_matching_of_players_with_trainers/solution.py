class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        N, M = len(players), len(trainers)
        res = 0
        j = 0
        players.sort()
        trainers.sort()
        
        for player in players:
            while j < M and player > trainers[j]:
                j += 1
            
            if j == M: break
            
            j += 1
            res += 1
        
        return res