class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def good(counter):
            for k, v in counter.items():
                if int(k) != v:
                    return False
            
            return True
        
        n += 1
        counter = collections.Counter(str(n))
        
        while not good(counter):
            n += 1
            counter = collections.Counter(str(n))
        
        return n