class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        N = len(skill)
        skill.sort()
        total = sum(skill)
        
        res = 0
        target = skill[0] + skill[-1]
        
        for i in range(N // 2):
            a, b = skill[i], skill[-i-1]
            if a + b != target: return -1
            res += a * b
        
        return res
            