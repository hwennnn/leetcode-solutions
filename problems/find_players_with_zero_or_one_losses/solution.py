class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        res = [[] for _ in range(2)]

        for winner, loser in matches:
            if winner not in loses:
                loses[winner] = 0
            
            if loser not in loses:
                loses[loser] = 1
            else:
                loses[loser] += 1

        for player, loseCount in loses.items():
            if loseCount == 0:
                res[0].append(player)
            elif loseCount == 1:
                res[1].append(player)

        res[0].sort()
        res[1].sort()

        return res