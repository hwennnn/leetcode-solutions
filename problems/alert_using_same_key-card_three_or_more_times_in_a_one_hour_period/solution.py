class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        res = set()
        
        def convertTime(time):
            return int("".join(time.split(':')))
        
        mp = collections.defaultdict(list)
        
        for name,time in zip(keyName, keyTime):
            mp[name].append(convertTime(time))
            
        for name in mp:
            time = sorted(mp[name])
            deq = collections.deque()
            c = 0
            
            for t in time:
                
                while deq and t - deq[0] > 100:
                    deq.popleft()
                    if c > 0:
                        c -= 1
                
                c += 1
                deq.append(t)
                
                if c >= 3:
                    res.add(name)
                    break
        
        return sorted(list(res))
                