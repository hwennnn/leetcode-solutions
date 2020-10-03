class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def convertTime(time):
            return int("".join(time.split(":")))
        
        
        dic = {}
        
        for name,time in zip(keyName,keyTime):
            time = convertTime(time)

            if name not in dic:
                dic[name] = [time]
            else:
                dic[name].append(time)

        res = []
        
        for name in dic:
            timeList = sorted(dic[name])
            tmp = []
            c = 0
            
            for time in timeList:
                
                while tmp and time - tmp[0] > 100:
                    tmp.pop(0)
                    if c > 0:
                        c -= 1
                        
                c += 1
                tmp.append(time)
                
                if c >= 3:
                    res.append(name)
                    break

        return sorted(res)
                    
            