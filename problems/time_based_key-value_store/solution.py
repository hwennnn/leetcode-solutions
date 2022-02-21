class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if len(self.mp[key]) == 0:
            self.mp[key].append((0, ""))
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.mp[key]) == 0: return ""
        
        index = bisect.bisect(self.mp[key], (timestamp + 1, )) - 1
            
        if self.mp[key][index][0] > timestamp:
            return ""
        
        return self.mp[key][index][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)