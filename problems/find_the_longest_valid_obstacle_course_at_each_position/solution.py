class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        res = []
        
        for obs in obstacles:
            if len(lis) == 0 or lis[-1] <= obs:
                lis.append(obs)
                res.append(len(lis))
            else:
                index = bisect.bisect(lis, obs)
                lis[index] = obs
                res.append(index + 1)
            
        return res