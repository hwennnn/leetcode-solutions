class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for word in strs:
            s = "".join(sorted(word))
            res[s].append(word)
        
        return res.values()