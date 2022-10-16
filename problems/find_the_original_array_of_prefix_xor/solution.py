class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N = len(pref)
        res = [pref[0]]

        for i in range(1, N):
            res.append(pref[i] ^ pref[i - 1])
                
        return res