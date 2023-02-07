class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        res = 0
        mp = defaultdict(int)
        i = 0

        for j, x in enumerate(fruits):
            mp[x] += 1

            while len(mp) > 2:
                if mp[fruits[i]] == 1:
                    del mp[fruits[i]]
                else:
                    mp[fruits[i]] -= 1
                    
                i += 1

            res = max(res, j - i + 1)

        return res