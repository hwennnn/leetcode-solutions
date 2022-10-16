class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        
        dontspeak = set()
        for u,v in friendships:
            u -= 1
            v -= 1
            
            if languages[u] & languages[v]: continue
            
            dontspeak.add(u)
            dontspeak.add(v)
        
        speak = Counter()
        for p in dontspeak:
            for l in languages[p]:
                speak[l] += 1
        
        return 0 if len(dontspeak) == 0 else len(dontspeak) - max(speak.values())