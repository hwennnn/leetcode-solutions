class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        N, M = len(robot), len(factory)
        INF = 10 ** 20
        robot.sort()
        factory.sort()

        @cache
        def go(i, j, k):
            if i == N: return 0
            
            res = INF

            if k > 0:
                res = min(res, go(i + 1, j, k - 1) + abs(factory[j][0] - robot[i]))
            
            if j + 1 < M:
                res = min(res, go(i, j + 1, factory[j + 1][1]))

            return res
        
        return go(0, 0, factory[0][1])

