class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, pn = len(req_skills), len(people)
        mp = {x: i for i, x in enumerate(req_skills)}

        dp = {0 : []}
        
        for index, skills in enumerate(people):
            mask = sum(1 << mp[skill] for skill in skills)
            
            for mask2, need in list(dp.items()):
                combined = mask | mask2
                
                if combined == mask2: continue
                
                if combined not in dp or len(dp[combined]) > len(need) + 1:
                    dp[combined] = need + [index]
                    
        return dp[(1 << n) - 1]