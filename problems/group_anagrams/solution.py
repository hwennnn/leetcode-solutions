class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        
        for word in strs:
            w = "".join(sorted(word))
            mp[w].append(word)
        
        return mp.values()