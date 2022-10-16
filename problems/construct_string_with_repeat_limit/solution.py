class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        n = len(s)
        words = Counter(s)
        heap = []
        res = ""
        last = (None, 0)
        
        for k, v in words.items():
            heapq.heappush(heap, (-ord(k), v))
        
        
        while len(heap) > 0:
            c, v = heapq.heappop(heap)
            c = -c

            if chr(c) == last[0]:
                count = min(repeatLimit, v) - last[1]
                if count <= 0: 
                    v = 0
                    continue
                v -= count
                res += chr(c) * count
                last = (chr(c), count)
            else:
                count = min(repeatLimit, v)
                v -= count
                res += chr(c) * count
                last = (chr(c), count)
            
            if heap and count == repeatLimit and v != 0:
                c2, v2 = heapq.heappop(heap)
                c2 = -c2
                # print(chr(c), v, chr(c2), v2)
                res += chr(c2) * 1
                v2 -= 1
                if v2 > 0:
                    heapq.heappush(heap, (-c2, v2))
                last = (chr(c2), 1)
            
            if v > 0:
                heapq.heappush(heap, (-c, v))
            



        return res
        
        