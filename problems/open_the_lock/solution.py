class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        forbidden = set(deadends)
        begin, end = set(['0000']), set([target])
        level = 0
        
        while begin and end:
            tmp = set()
            
            for lock in begin:
                if lock in forbidden: continue
                    
                if lock in end: return level

                forbidden.add(lock)

                for i in range(4):
                    w1 = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:]
                    w2 = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i + 1:]

                    for p in (w1, w2):
                        if p not in forbidden:
                            tmp.add(p)
                            
            begin = end
            end = tmp
            level += 1
            
        return -1